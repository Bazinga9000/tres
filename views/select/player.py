from typing import override
from discord import Member, User
from discord.ui import Select, View
from .base import BaseSelect


class PlayerSelect(BaseSelect[User | Member]):
    @override
    def initialize_select(self) -> Select[View]:
        select = Select[View](placeholder='Select a player.')
        for player in self.game.players:
            select.add_option(label=player.display_name, value=str(player.id))
        return select
    
    @override
    def get_value(self) -> User | Member:
        if not self.select.values:
            raise ValueError('No player selected.')
        player = self.game.find_player_id(int(str(self.select.values[0])))
        if player is None:
            raise ValueError('Selected player not found in game.')
        return player