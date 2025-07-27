from collections.abc import Callable
from typing import Coroutine
import discord
import game_db
import random
from pregame import PreGame
from game_components import Player
from views.cardview import CardView
from game_components.decks import TestDeck

class Game:
    def __init__(self, pregame: PreGame):
        # Overwrite the pregame with the real game
        self.uuid = pregame.uuid
        game_db.games[self.uuid] = self

        self.players = [Player(i) for i in pregame.players]
        self.channel = pregame.channel
        self.name = pregame.name

        # Set up game
        self.round = 1
        self.turn = 1

        random.shuffle(self.players)
        self.whose_turn = 0

        # todo more robust deck implementation (for e.g procedural deck)
        self.deck = TestDeck()

        for p in self.players:
            for _ in range(7):
                p.hand.add_card(self.deck.draw_from_deck())

        self.piles = [[self.deck.draw_from_deck()]]

        # Card Debt = cards that must be drawn by the next player in lieu of taking a turn
        self.card_debt = 0

    @property
    def active_player(self):
        return self.players[self.whose_turn]

    # Called at the start of a game
    async def on_start(self):
        await self.start_turn()

    # Sends the message signalling the start of a new turn
    async def start_turn(self):
        # Generate the embed
        e = discord.Embed(
            title=f"Tres - {self.name}",
            description=f"Turn {self.turn}",
            color=discord.Colour.blurple(),
        )

        # Turn order graphic (text for now)
        turn_order = " > ".join(f"**{u.display_name}**" if i == self.whose_turn else u.display_name for (i,u) in enumerate(self.players))
        e.add_field(name="Turn Order", value=turn_order)

        e.add_field(name="Your Hand", value=self.active_player.hand.display_all_cards())

        e.add_field(name="Top Card", value=self.piles[0][-1].display_name)

        await self.channel.send(embed = e, view = TurnStarterView(self))


    # Performs cleanup at the end of a turn and then starts the next turn if needed
    async def end_turn(self):
        if len(self.active_player.hand) == 0:
            # Assign penalty points
            for p in self.players:
                # todo: cards might fuck with penalty points more than just adding them
                for c in p.hand:
                    p.score += c.penalty_points

            self.round += 1
            self.turn = 1
            game_db.games[self.uuid] = None # End the game (that is, remove it from the database)
            await self.channel.send(f"The game is over! **{self.active_player.display_name}** has won!")
            # todo - sort this
            await self.channel.send(f"**Final Scores**\n{'\n'.join(f"{p.display_name} - {p.score} points" for p in self.players)}")
        else:
            self.whose_turn = (self.whose_turn + 1) % len(self.players)
            self.turn += 1
            await self.start_turn()

    # Draw n cards into a player's hand
    def draw_card(self, player: Player, n: int = 1):
        for _ in range(n):
            c = self.deck.draw_from_deck()
            player.hand.add_card(c)
            c.on_draw(self, player)

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
        self.player = game.active_player

    # Wrap a callback to validate the turn
    # The actual callbacks are thus assumed to be correct
    def is_bad(self):
        return (self.game.round, self.game.turn) != (self.round, self.turn)

    # Delete the entire message if the interaction is done out of turn
    def delete_out_of_turn(self, cb: Callable[[discord.Interaction], Coroutine[None, None, None]]):
        async def wrapper(interaction: discord.Interaction):
            if self.is_bad():
                # This view is no longer required. Kill the message!
                await interaction.response.defer()
                await interaction.delete_original_response()
                self.stop()
                return
            await cb(interaction)
        return wrapper

    # Empty the view if the interaction is done out of turn, but do not delete the message
    def empty_out_of_turn(self, cb: Callable[[discord.Interaction], Coroutine[None, None, None]]):
        async def wrapper(interaction: discord.Interaction):
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
        turn_button: discord.ui.Button[TurnTrackingView] = discord.ui.Button(label=f"Take Turn ({self.player.display_name})", row=1, style=discord.ButtonStyle.blurple)
        turn_button.callback = self.empty_out_of_turn(self.turn_callback)
        self.add_item(turn_button)


    async def turn_callback(self, interaction: discord.Interaction):
        if interaction.user is None:
            await interaction.respond("Who am I talking to? Am I just a ghost in the machine? What is life?")
            return
        if interaction.user.id != self.player.id:
            await interaction.respond("It's not your turn!", ephemeral=True)
            return

        await interaction.respond(view=CardView(self.game), ephemeral=True)
        return
