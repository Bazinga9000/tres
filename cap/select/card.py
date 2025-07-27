from typing import TYPE_CHECKING, Any, override

from discord.ui import Select, View
from .base import BaseSelect

if TYPE_CHECKING:
    from card import Card
else:
    Card = Any


class CardSelect(BaseSelect[Card]):
    @override
    def initialize_select(self) -> Select[View]:
        select = Select[View](placeholder='Select a card.')
        for index, card in enumerate(self.game.hands[self.game.players[self.game.whose_turn]]):
            select.add_option(label=card.display_name, value=str(index))
        return select
    
    @override
    def get_value(self) -> Card:
        if not self.select.values:
            raise ValueError("No card selected.")
        index = int(str(self.select.values[0]))
        hand = self.game.hands[self.game.players[self.game.whose_turn]]
        if not 0 <= index < len(hand):
            raise ValueError("Selected card index out of range.")
        return hand[index]
