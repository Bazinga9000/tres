from typing import override
from discord.ui import Select, View
from card import CardColor
from .base import BaseSelect


class ColorSelect(BaseSelect[CardColor]):
    @override
    def initialize_select(self) -> Select[View]:
        select = Select[View](placeholder='Select a color.')
        for color in CardColor:
            select.add_option(label=(color.name or '???').capitalize(), value=str(color.value))
        return select
    
    @override
    def get_value(self) -> CardColor:
        if not self.select.values:
            raise ValueError('No color selected.')
        return CardColor(int(str(self.select.values[0])))
