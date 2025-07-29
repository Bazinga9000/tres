from typing import override

from card import Card, CardColor
from . import Game
from views.argbuilder import ArgBuilder


class WildNumber(Card):
    def __init__(self, c: CardColor):
        super().__init__(c, 40, 0, "wild_number", False)

    @property
    @override
    def args(self):
        return ArgBuilder[Game]().add_number(min=0, max=15).with_callback(self.on_play)

    def on_play(self, game: Game, n: int):
        # todo: other cards might now treat this identically to its given number
        # since we're setting its card type directly to that of a number card
        # we might want to have some more intelligent behavior?
        # even if we want it so bouncing this card after it is declared an X means
        # you can only play it on its color or X, and then change its number later
        self.card_type = str(n)
        self.number_value = n
        self.display_name = f'{self.display_name} ({n})'
