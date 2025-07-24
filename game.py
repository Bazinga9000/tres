import discord
import game_db
import random
from card.number_card import NumberCard
from card.color import CardColor

class Game:
    def __init__(self, pregame):
        # Overwrite the pregame with the real game
        self.uuid = pregame.uuid
        game_db.games[self.uuid] = self

        self.players = pregame.players
        self.channel = pregame.channel
        self.name = pregame.name

        # Set up game
        self.turn = 1

        random.shuffle(self.players)
        self.whose_turn = 0

        # todo more robust deck implementation (for e.g procedural deck)
        self.deck = []
        for c in [CardColor.RED, CardColor.ORANGE, CardColor.YELLOW, CardColor.GREEN, CardColor.BLUE, CardColor.PURPLE]:
            for n in range(1,16):
                self.deck.append(NumberCard(c,n))
        random.shuffle(self.deck)

        self.hands = {}
        for p in self.players:
            self.hands[p] = [self.deck.pop() for _ in range(7)]

        self.piles = [[self.deck.pop()]]

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

        v = discord.ui.View()

        async def turn_callback(interaction):
            if interaction.user != active_player:
                return await interaction.respond("It's not your turn!", ephemeral=True)

            await interaction.respond(view=self.card_play_view(active_player), ephemeral=True)


        turn_button = discord.ui.Button(label=f"Take Turn ({active_player.display_name})", row=1, style=discord.ButtonStyle.blurple)
        turn_button.callback = turn_callback
        v.add_item(turn_button)

        await self.channel.send(embed = e, view = v)

    # Generates the view that allows a player to play a card
    def card_play_view(self, player, can_pass=False):
        v = discord.ui.View()

        playable = []
        for cn,c in enumerate(self.hands[player]):
            for pn in range(len(self.piles)):
                if c.can_play(self, pn):
                    playable.append(discord.SelectOption(
                        label = f"{c.display_name} onto pile #{pn+1}",
                        value = f"{cn},{pn}" # Values can only be strings, so this is easily parseable int,int
                    ))

        if len(playable) == 0:
            # No need to add the modal/button for playing a card, no cards to play
            draw_button = discord.ui.Button(label = "Draw a card", style = discord.ButtonStyle.danger)
            async def draw_callback(interaction):
                self.hands[player].append(self.deck.pop())
                await self.channel.send(f"{player.display_name} drew a card!")
                await interaction.edit(view=self.card_play_view(player, can_pass=True))

            draw_button.callback = draw_callback

            pass_button = discord.ui.Button(label = "Pass turn", style = discord.ButtonStyle.blurple)
            async def pass_callback(interaction):
                await self.channel.send(f"{player.display_name} passed their turn!")
                await interaction.response.defer()
                await interaction.delete_original_response()
                await self.end_turn()
            pass_button.callback = pass_callback

            v.add_item(draw_button)
            if can_pass: v.add_item(pass_button)

            return v

        s = discord.ui.Select(
            placeholder = "Select a card to play...",
            min_values = 1,
            max_values = 1,
            options = playable
        )

        async def select_callback(interaction):
            chosen = s.values[0].split(",") # pyright: ignore (split is safe, all values will be strings)
            chosen_card_idx = int(chosen[0])
            chosen_pile = int(chosen[1])

            chosen_card = self.hands[player].pop(chosen_card_idx)
            self.piles[chosen_pile].append(chosen_card)

            await interaction.response.defer()
            await interaction.delete_original_response()
            await self.end_turn()

        s.callback = select_callback
        v.add_item(s)

        return v

    # Performs cleanup at the end of a turn and then starts the next turn if needed
    async def end_turn(self):
        active_player = self.players[self.whose_turn]
        if len(self.hands[active_player]) == 0:
            # todo: actual point values and multi-round games
            game_db.games[self.uuid] = None # End the game (that is, remove it from the database)
            await self.channel.send(f"The game is over! **{active_player.display_name}** has won!")
        else:
            self.whose_turn = (self.whose_turn + 1) % len(self.players)
            self.turn += 1
            await self.start_turn()
