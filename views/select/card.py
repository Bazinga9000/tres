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
        for card in self.game.hands[self.game.players[self.game.whose_turn]]:
            if card.playable_piles(self.game) or not requires_playable:
                self.select.add_option(label=card.display_name, value=str(card.uuid))
    
    @override
    def get_value(self) -> Card:
        uuid = UUID(self.get_raw_value())
        hand = self.game.hands[self.game.players[self.game.whose_turn]]
        card = hand.lookup_card(uuid)
        if not card:
            raise ValueError("Selected card index out of range.")
        return card
