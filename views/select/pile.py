from typing import TYPE_CHECKING, Any, override
from .base import BaseSelect

if TYPE_CHECKING:
    from card import Card
    from game import Game
else:
    Card = Game = Any


class PileSelect(BaseSelect[int]):
    def __init__(self, game: Game, placeholder: str, *, playable_by: Card | None):
        super().__init__(game, placeholder)
        for i in range(len(self.game.piles)):
            if not playable_by or playable_by.can_play(self.game, i):
                self.select.add_option(label=f'Pile #{i + 1}', value=str(i))
    
    @override
    def get_value(self) -> int:
        pile = int(self.get_raw_value())
        if not 0 <= pile < len(self.game.piles):
            raise ValueError('Selected pile index out of range.')
        return pile
