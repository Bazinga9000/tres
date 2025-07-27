from typing import TYPE_CHECKING, Any, override
from uuid import UUID

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
        for card in self.game.hands[self.game.players[self.game.whose_turn]]:
            select.add_option(label=card.display_name, value=str(card.uuid))
        return select
    
    @override
    def get_value(self) -> Card:
        if not self.select.values:
            raise ValueError("No card selected.")
        uuid = UUID(str(self.select.values[0]))
        hand = self.game.hands[self.game.players[self.game.whose_turn]]
        card = hand.lookup_card(uuid)
        if not card:
            raise ValueError("Selected card index out of range.")
        return card
