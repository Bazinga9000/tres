import discord
import uuid


class GameJoinerView(discord.ui.View):
    def __init__(self, uns_game):
        super().__init__()
        self.uns_game = uns_game

    async def update_info(self, interaction):
        out = "**Players:**\n" + "\n".join([str(u.display_name) for u in self.uns_game.players])
        await interaction.edit(content=out, view=self)

    @discord.ui.button(label="Join Game", row=1, style=discord.ButtonStyle.success)
    async def join_callback(self, button, interaction):
        if interaction.user in self.uns_game.players:
            await interaction.respond("You are already in the game!", ephemeral=True)
        else:
            self.uns_game.players.append(interaction.user)
            await self.update_info(interaction)

    @discord.ui.button(label="Leave Game", row=1, style=discord.ButtonStyle.danger)
    async def leave_callback(self, button, interaction):
        if interaction.user not in self.uns_game.players:
            await interaction.respond("You are not in the game!", ephemeral=True)
        else:
            self.uns_game.players.remove(interaction.user)
            await self.update_info(interaction)

class UnstartedGame():
    def __init__(self):
        self.uuid = uuid.uuid4()
        self.players = []
        self.view = GameJoinerView(self)
