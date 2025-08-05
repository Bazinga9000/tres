import discord
from game_components.hand import Hand
from typing import Self

class Player:
    def __init__(self, discord_user: discord.Member | discord.User):
        self.discord_user = discord_user
        self.id = discord_user.id
        self.score = 0
        self.hand = Hand()
        self.ejected = False
        self.eliminated = False

    @property
    def display_name(self) -> str:
        return self.discord_user.display_name

    def formatted_display_name(self, active_player: Self) -> str:
        '''
        Returns the player's display name, formatted for discord markdown.

        If the player is the active player, their name will be **bold**.
        If the player is ejected, their name will be ~~struckthrough~~.
        '''
        if self.ejected:
            return f"~~{self.display_name}~~"
        elif self == active_player:
            return f"**{self.display_name}**"
        else:
            return self.display_name

    @property
    def display_avatar(self) -> discord.Asset:
        return self.discord_user.display_avatar

    def eject(self):
        '''
        Mark this player as ejected and add their hand's penalty value to their score
        '''
        self.ejected = True
        self.score += self.hand.penalty_value()
