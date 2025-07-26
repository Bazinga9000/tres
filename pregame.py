from typing import Self
import discord
import uuid
import game_db
import game

class PreGame(discord.ui.View):
    def __init__(self, host: discord.User | discord.Member, channel: discord.TextChannel, name: str | None):
        super().__init__()

        # Generate a UUID for this game and add it to the global DB
        self.uuid = uuid.uuid4()
        game_db.games[self.uuid] = self

        # The person who started the game
        self.host = host

        # The channel in which the game is being played
        self.channel = channel

        # The name of the game
        if name is None:
            self.name = f"Game {self.uuid}"
        else:
            self.name = name

        # Players in the game
        self.players = [self.host]

    def info_embed(self):
        embed = discord.Embed(
            title="Tres",
            description=f"{self.name}",
            color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
        )

        player_list = "*No players yet.*" if len(self.players) == 0 else ", ".join([str(u.display_name) for u in self.players])
        player_field_name = "**Players**" if len(self.players) == 0 else f"**Players ({len(self.players)})**"
        embed.add_field(name=player_field_name, value=player_list)

        return embed


    # Interactions
    @discord.ui.button(label="Start Game", row=0, style=discord.ButtonStyle.blurple)
    async def start_callback(self, button: discord.ui.Button[Self], interaction: discord.Interaction):
        if interaction.user != self.host:
            return await interaction.respond("Only the host can start the game!", ephemeral=True)

        if len(self.players) == 0:
            return await interaction.respond("You can't start a game with zero players in it!", ephemeral=True)

        # Generate a full game from this pregame (the init will automatically overwrite the DB)
        started_game = game.Game(self)
        self.disable_all_items()
        await interaction.edit(embed=self.info_embed(), view=self)
        await started_game.on_start()

    async def update_info(self, interaction: discord.Interaction):
        await interaction.edit(embed=self.info_embed(), view=self)

    @discord.ui.button(label="Join Game", row=1, style=discord.ButtonStyle.success)
    async def join_callback(self, button: discord.ui.Button[Self], interaction: discord.Interaction):
        if interaction.user in self.players:
            await interaction.respond("You are already in the game!", ephemeral=True)
        elif interaction.user:
            self.players.append(interaction.user)
            await self.update_info(interaction)

    @discord.ui.button(label="Leave Game", row=1, style=discord.ButtonStyle.danger)
    async def leave_callback(self, button: discord.ui.Button[Self], interaction: discord.Interaction):
        if interaction.user not in self.players:
            await interaction.respond("You are not in the game!", ephemeral=True)
        elif interaction.user:
            self.players.remove(interaction.user)
            await self.update_info(interaction)
