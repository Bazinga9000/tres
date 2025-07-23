import discord
import uuid

class PreGame(discord.ui.View):
    def __init__(self, name):
        super().__init__()
        self.uuid = uuid.uuid4()
        self.players = []

        if name is None:
            self.name = f"Game {self.uuid}"
        else:
            self.name = name

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
    async def update_info(self, interaction):
        await interaction.edit(embed=self.info_embed(), view=self)

    @discord.ui.button(label="Join Game", row=1, style=discord.ButtonStyle.success)
    async def join_callback(self, button, interaction):
        if interaction.user in self.players:
            await interaction.respond("You are already in the game!", ephemeral=True)
        else:
            self.players.append(interaction.user)
            await self.update_info(interaction)

    @discord.ui.button(label="Leave Game", row=1, style=discord.ButtonStyle.danger)
    async def leave_callback(self, button, interaction):
        if interaction.user not in self.players:
            await interaction.respond("You are not in the game!", ephemeral=True)
        else:
            self.players.remove(interaction.user)
            await self.update_info(interaction)
