from typing import TYPE_CHECKING, Any, override
from uuid import UUID


from .base import BaseSelect

if TYPE_CHECKING:
    from card import Card
    from game import Game
else:
    Card = Game = Any


class CardSelect(BaseSelect[Card]):
    def __init__(self, game: Game, placeholder: str, *, requires_playable: bool):
        super().__init__(game, placeholder)
        for card in self.game.active_player.hand:
            if card.playable_piles(self.game) or not requires_playable:
                self.select.add_option(label=card.display_name, value=str(card.uuid))

    @override
    def get_value(self) -> Card:
        card = self.game.active_player.hand.lookup_card(UUID(self.get_raw_value()))
        if not card:
            raise ValueError("Selected card index out of range.")
        return card
