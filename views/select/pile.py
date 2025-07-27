from typing import override
from discord.ui import Select, View
from .base import BaseSelect


class PileSelect(BaseSelect[int]):
    @override
    def initialize_select(self) -> Select[View]:
        select = Select[View](placeholder='Select a pile.')
        for i in range(len(self.game.piles)):
            select.add_option(label=f'Pile #{i + 1}', value=str(i))
        return select
    
    @override
    def get_value(self) -> int:
        if not self.select.values:
            raise ValueError('No pile selected.')
        pile = int(str(self.select.values[0]))
        if not 0 <= pile < len(self.game.piles):
            raise ValueError('Selected pile index out of range.')
        return pile
