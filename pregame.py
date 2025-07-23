import discord
import uuid


class GameJoinerView(discord.ui.View):
    def __init__(self, pg):
        super().__init__()
        self.pg = pg

    async def update_info(self, interaction):
        out = "**Players:**\n" + "\n".join([str(u.display_name) for u in self.pg.players])
        await interaction.edit(content=out, view=self)

    @discord.ui.button(label="Join Game", row=1, style=discord.ButtonStyle.success)
    async def join_callback(self, button, interaction):
        if interaction.user in self.pg.players:
            await interaction.respond("You are already in the game!", ephemeral=True)
        else:
            self.pg.players.append(interaction.user)
            await self.update_info(interaction)

    @discord.ui.button(label="Leave Game", row=1, style=discord.ButtonStyle.danger)
    async def leave_callback(self, button, interaction):
        if interaction.user not in self.pg.players:
            await interaction.respond("You are not in the game!", ephemeral=True)
        else:
            self.pg.players.remove(interaction.user)
            await self.update_info(interaction)

class PreGame():
    def __init__(self):
        self.uuid = uuid.uuid4()
        self.players = []
        self.view = GameJoinerView(self)
