import discord
import game_db
import random

class Game:
    def __init__(self, pregame):
        # Overwrite the pregame with the real game
        self.uuid = pregame.uuid
        game_db.games[self.uuid] = self

        self.players = pregame.players
        self.channel = pregame.channel
        self.name = pregame.name

        self.turn = 1

        random.shuffle(self.players)
        self.active_player = 0

    async def on_start(self):
        await self.start_turn()

    async def start_turn(self):
        # Generate the embed
        e = discord.Embed(
            title=f"Tres - {self.name}",
            description=f"Turn {self.turn}",
            color=discord.Colour.blurple(),
        )

        # Turn order graphic (text for now)
        turn_order = " > ".join(f"**{u.display_name}**" if i == self.active_player else u.display_name for (i,u) in enumerate(self.players))
        e.add_field(name="Turn Order", value=turn_order)

        # The view which contains the "Take your turn" button which will eventually throw up an ephemeral modal
        v = discord.ui.View()

        async def turn_callback(view, button, interaction):
            if interaction.user != self.players[self.active_player]:
                return await interaction.respond("It's not your turn!", ephemeral=True)

            self.active_player = (self.active_player + 1) % len(self.players)
            self.turn += 1
            view.clear_items()
            await interaction.edit(embed=e, view=view)
            await self.start_turn()

        turn_button = discord.ui.Button(label=f"Take Turn ({self.players[self.active_player].display_name})", row=1, style=discord.ButtonStyle.blurple)
        turn_button.callback = lambda interaction: turn_callback(v, turn_button, interaction)
        v.add_item(turn_button)

        await self.channel.send(embed = e, view = v)
