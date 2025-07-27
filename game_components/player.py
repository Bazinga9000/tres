import discord
from game_components.hand import Hand

class Player:
    def __init__(self, discord_user: discord.Member | discord.User):
        self.discord_user = discord_user
        self.id = discord_user.id
        self.score = 0
        self.hand = Hand()

    @property
    def display_name(self) -> str:
        return self.discord_user.display_name

    @property
    def display_avatar(self) -> discord.Asset:
        return self.discord_user.display_avatar
