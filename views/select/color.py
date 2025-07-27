from typing import TYPE_CHECKING, Any, override
from card import CardColor
from .base import BaseSelect

if TYPE_CHECKING:
    from game import Game
else:
    Game = Any


class ColorSelect(BaseSelect[CardColor]):
    def __init__(self, game: Game, placeholder: str):
        super().__init__(game, placeholder)
        for color in CardColor:
            self.select.add_option(label=(color.name or '???').capitalize(), value=str(color.value))
    
    @override
    def get_value(self) -> CardColor:
        return CardColor(int(self.get_raw_value()))
