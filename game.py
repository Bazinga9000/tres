import discord
from card.abc import Card
from card.reverse_card import ReverseCard
from card.reverse_skip import ReverseSkipCard
from card.skip_card import SkipCard
from card.wild_card import WildCard, WildDrawCard
import game_db
import random
from card.number_card import NumberCard
from card.basic_draw_card import DrawCard
from card.color import CardColor
import card.card_arg as ca

class Game:
    def __init__(self, pregame):
        # Overwrite the pregame with the real game
        self.uuid = pregame.uuid
        game_db.games[self.uuid] = self

        self.players = pregame.players
        self.channel = pregame.channel
        self.name = pregame.name

        # Set up game
        self.round = 1
        self.turn = 1

        random.shuffle(self.players)
        self.whose_turn = 0

        # todo more robust deck implementation (for e.g procedural deck)
        self.deck = []
        for c in [CardColor.RED, CardColor.ORANGE, CardColor.YELLOW, CardColor.GREEN, CardColor.BLUE, CardColor.PURPLE]:
            for n in range(1,16):
                self.deck.append(NumberCard(c,n))
            for _ in range(2):
                self.deck.append(DrawCard(c, 2))     # Draw 2s
                self.deck.append(ReverseCard(c))     # Reverse
                self.deck.append(SkipCard(c))        # Single Skip
                self.deck.append(ReverseSkipCard(c)) # Reverse Skip
                self.deck.append(WildDrawCard(4))    # Wild Draw 4
            for _ in range(5):
                self.deck.append(WildCard())                # Wild Cards
            self.deck.append(NumberCard(CardColor.RED, 40)) # Red 40

        random.shuffle(self.deck)

        self.hands = {}
        for p in self.players:
            self.hands[p] = [self.deck.pop() for _ in range(7)]

        self.piles = [[self.deck.pop()]]

        # Card Debt = cards that must be drawn by the next player in lieu of taking a turn
        self.card_debt = 0

    # Called at the start of a game
    async def on_start(self):
        await self.start_turn()

    # Sends the message signalling the start of a new turn
    async def start_turn(self):
        active_player = self.players[self.whose_turn]
        # Generate the embed
        e = discord.Embed(
            title=f"Tres - {self.name}",
            description=f"Turn {self.turn}",
            color=discord.Colour.blurple(),
        )

        # Turn order graphic (text for now)
        turn_order = " > ".join(f"**{u.display_name}**" if i == self.whose_turn else u.display_name for (i,u) in enumerate(self.players))
        e.add_field(name="Turn Order", value=turn_order)

        hand = "\n".join(c.display_name for c in self.hands[active_player])
        e.add_field(name="Your Hand", value=hand)

        e.add_field(name="Top Card", value=self.piles[0][-1].display_name)

        await self.channel.send(embed = e, view = TurnStarterView(self))


    # Performs cleanup at the end of a turn and then starts the next turn if needed
    async def end_turn(self):
        active_player = self.players[self.whose_turn]
        if len(self.hands[active_player]) == 0:
            # todo: actual point values
            self.round += 1
            self.turn = 1
            game_db.games[self.uuid] = None # End the game (that is, remove it from the database)
            await self.channel.send(f"The game is over! **{active_player.display_name}** has won!")
        else:
            self.whose_turn = (self.whose_turn + 1) % len(self.players)
            self.turn += 1
            await self.start_turn()

    # Draw n cards into a player's hand
    def draw_card(self, player, n=1):
        for _ in range(n):
            c = self.deck.pop()
            c.on_draw(self, player)
            self.hands[player].append(c)
        # todo: sort hands here

    def find_player_id(self, player_id: int):
        for p in self.players:
            if p.id == player_id:
                return p

        return None

# A view that can keep track of the game's turns, and disable callbacks if they're out of turn
class TurnTrackingView(discord.ui.View):
    def __init__(self, game: Game):
        super().__init__()
        self.game = game
        self.turn = game.turn
        self.round = game.round
        self.player = game.players[game.whose_turn]

    # Wrap a callback to validate the turn
    # The actual callbacks are thus assumed to be correct
    def is_bad(self):
        return (self.game.round, self.game.turn) != (self.round, self.turn)

    # Delete the entire message if the interaction is done out of turn
    def delete_out_of_turn(self, cb):
        async def wrapper(interaction):
            if self.is_bad():
                # This view is no longer required. Kill the message!
                await interaction.response.defer()
                await interaction.delete_original_response()
                self.stop()
                return
            await cb(interaction)
        return wrapper

    # Empty the view if the interaction is done out of turn, but do not delete the message
    def empty_out_of_turn(self, cb):
        async def wrapper(interaction):
            if self.is_bad():
                # This view is no longer required. Remove it from the message!
                await interaction.edit(view=None)
                self.stop()
                return
            await cb(interaction)
        return wrapper

class TurnStarterView(TurnTrackingView):
    def __init__(self, game: Game):
        super().__init__(game)
        turn_button = discord.ui.Button(label=f"Take Turn ({self.player.display_name})", row=1, style=discord.ButtonStyle.blurple)
        turn_button.callback = self.empty_out_of_turn(self.turn_callback)
        self.add_item(turn_button)


    async def turn_callback(self, interaction):
        if interaction.user != self.player:
            return await interaction.respond("It's not your turn!", ephemeral=True)

        await interaction.respond(view=ActivePlayerView(self.game), ephemeral=True)

# The view shown to the active player in an ephemeral message to play cards/choose targets/etc
class ActivePlayerView(TurnTrackingView):
    def __init__(self, game: Game):
        super().__init__(game)
        # Can this player pass their turn?
        self.can_pass = False

        # Which card does the player want to play?
        self.selected_card_index = None
        # Where do they want to play it?
        self.selected_pile = None

        # Set up the core buttons
        # Draw a card
        self.draw_button = discord.ui.Button(label = "Draw a card", style = discord.ButtonStyle.danger)
        self.draw_button.callback = self.delete_out_of_turn(self.draw_callback)
        self.add_item(self.draw_button)
        # Pass your turn
        self.pass_button = discord.ui.Button(label = "Pass turn", style = discord.ButtonStyle.blurple)
        self.pass_button.callback = self.delete_out_of_turn(self.pass_callback)
        self.add_item(self.pass_button)
        # Play a card
        self.play_button = discord.ui.Button(label = "Play selected card", style = discord.ButtonStyle.success)
        self.play_button.callback = self.delete_out_of_turn(self.play_callback)
        self.add_item(self.play_button)
        # Card selector (added in update_items if needed)
        self.card_selector = None
        # Update the core items, enabling/disabling if neeeded
        self.update_items(True)

        # A map of the card arg selectors currently in the item
        self.card_arg_selectors = {}
        self.card_arg_choices = {}



    # Update self and update the interaction
    async def update(self, interaction, refresh_selector):
        self.update_items(refresh_selector)
        await interaction.edit(view=self)

    # Update the items of this view
    def update_items(self, refresh_selector):
        g = self.game

        if g.card_debt > 0:
            self.draw_button.label = f"Pay Card Debt ({g.card_debt})"
            self.draw_button.callback = self.delete_out_of_turn(self.pay_card_debt_callback)
            self.can_pass = False
        else:
            self.draw_button.label = "Draw Card"
            self.draw_button.callback = self.delete_out_of_turn(self.draw_callback)

        self.pass_button.disabled = not self.can_pass
        self.play_button.disabled = not self.can_press_play()

        # Evaluate how many cards in the player's hand can be played, and where, and generate the requisite select options
        playable = []
        for cn,c in enumerate(g.hands[self.player]):
            for pn in range(len(g.piles)):
                if c.can_play(g, pn):
                    playable.append(discord.SelectOption(
                        label = f"{c.display_name} onto pile #{pn+1}",
                        value = f"{cn},{pn}" # Values can only be strings, so this is easily parseable int,int
                    ))

        if playable == []: # no playable cards, no need to mess with the select modal
            return

        if self.card_selector is None:
            self.card_selector = discord.ui.Select(
                placeholder = "Select a card to play...",
                min_values = 1,
                max_values = 1,
                options = playable
            )
            self.card_selector.callback = self.delete_out_of_turn(self.card_select_callback)
            self.add_item(self.card_selector)
            return

        if refresh_selector:
            self.card_selector.options = playable

    async def draw_callback(self, interaction):
        g = self.game
        g.draw_card(self.player, 1)
        self.can_pass = True
        await g.channel.send(f"{self.player.display_name} drew a card!")
        await self.update(interaction, True) # card was drawn, need to remake the card selector

    async def pay_card_debt_callback(self, interaction):
        g = self.game
        g.draw_card(self.player, g.card_debt)
        g.card_debt = 0
        await g.channel.send(f"{self.player.display_name} pays the card debt ({g.card_debt})!")
        await self.stop_view_and_end(interaction)



    async def pass_callback(self, interaction):
        g = self.game
        await g.channel.send(f"{self.player.display_name} passed their turn!")
        await self.stop_view_and_end(interaction)


    # Should the play button be enabled?
    def can_press_play(self):
        if self.selected_pile is None or self.selected_card_index is None: # If you haven't selected a card...
            return False # You definitely can't play.

        for v in self.card_arg_choices.values(): # If the selected card has any arguments...
            if v is None: # If the argument is unset...
                return False # you can't play the card yet

        return True

    async def play_callback(self, interaction):
        g = self.game

        chosen_card = g.hands[self.player].pop(self.selected_card_index)
        g.piles[self.selected_pile].append(chosen_card) # pyright: ignore (this is safe, selected_pile will be non-None at this point)
        chosen_card.on_play(g, self.selected_pile, self.card_arg_choices)
        await self.stop_view_and_end(interaction)

    async def card_select_callback(self, interaction):
        assert self.card_selector is not None
        raw_value = self.card_selector.values[0]
        chosen = self.card_selector.values[0].split(",") # pyright: ignore (split is safe, all values will be strings)
        self.selected_card_index = int(chosen[0])
        self.selected_pile = int(chosen[1])

        # Find the selected value, set it as default so view updates don't change it
        for o in self.card_selector.options:
            o.default = o.value == raw_value

        # Delete all existing card arg selectors and clear the choices dictionary
        for v in self.card_arg_selectors.values():
            self.remove_item(v)
        self.card_arg_choices = {}

        self.card_arg_selectors = self.make_card_arg_selectors(self.game.hands[self.player][self.selected_card_index])
        for (k,v) in self.card_arg_selectors.items():
            self.add_item(v)
            self.card_arg_choices[k] = None

        await self.update(interaction, False) # hand hasn't changed, no need to refresh the card selector's options


    # Utility function to delete the message and end the turn.
    async def stop_view_and_end(self, interaction):
        await interaction.response.defer()
        await interaction.delete_original_response()
        self.stop()
        await self.game.end_turn()

    def make_card_arg_selectors(self, card : Card):
        def make_selector(name: str, arg: ca.CardArg):
            type = arg.arg_type
            s = discord.ui.Select(
                select_type = discord.ComponentType.string_select,
                placeholder = arg.label,
                min_values = arg.min,
                max_values = arg.max
            )
            # Set the callback
            s.callback = self.make_arg_selector_callback(name, s, type)

            # Generate the options
            match type:
                case ca.CardArgType.Color:
                    for o in [
                        ("Red", CardColor.RED),
                        ("Orange", CardColor.ORANGE),
                        ("Yellow", CardColor.YELLOW),
                        ("Green", CardColor.GREEN),
                        ("Blue", CardColor.BLUE),
                        ("Purple", CardColor.PURPLE)
                    ]:
                        s.add_option(
                            label = o[0],
                            value = str(o[1].value)
                        )

                case ca.CardArgType.Player | ca.CardArgType.AnotherPlayer:
                    for p in self.game.players:
                        if p != self.player or type == ca.CardArgType.Player:
                            s.add_option(
                                label = p.display_name,
                                value = str(p.id)
                            )

                case ca.CardArgType.PlayableCard | ca.CardArgType.AnyCard:
                    for (k,c) in enumerate(self.game.hands[self.player]):
                        if c != card: # A card can never select itself
                            if type == ca.CardArgType.AnyCard or c.can_play(self.game, self.selected_pile):
                               s.add_option(
                                   label = c.display_name,
                                   value = str(k)
                               )

                case ca.CardArgType.Arbitrary:
                    for o in card.get_custom_arg_choices(name):
                        s.add_option(
                            label = o[0],
                            value = o[1]
                        )

                case _:
                    raise NotImplementedError(f"Card Arg Type {type} Not Yet Implemented")

            return s

        out = {}
        for (k,v) in card.get_args().items():
            out[k] = make_selector(k, v)
        return out

    def make_arg_selector_callback(self, choice_id: str, selector: discord.ui.Select, arg_type: ca.CardArgType):
        # Get the "parser function" that converts the selectors String/User value into the actual value choice
        parser = {
            ca.CardArgType.Color: lambda v: CardColor(int(v)), # Shove the integer into the color enum directly
            ca.CardArgType.PlayableCard: lambda v: self.game.hands[self.player][int(v)], # nth card in player's hand
            ca.CardArgType.AnyCard: lambda v: self.game.hands[self.player][int(v)],
            ca.CardArgType.AnotherPlayer: lambda v: self.game.find_player_id(int(v)), # uses player ID
            ca.CardArgType.Player: lambda v: self.game.find_player_id(int(v)),
            ca.CardArgType.Arbitrary: lambda v: v # do nothing to arbitrary type
        }[arg_type]

        async def callback(interaction):
            # Set the arg choices
            self.card_arg_choices[choice_id] = [parser(v) for v in selector.values]
            # Set the defaults
            for o in selector.options:
                o.default = o.value in selector.values
            # update the view
            await self.update(interaction, False)

        return self.delete_out_of_turn(callback)
