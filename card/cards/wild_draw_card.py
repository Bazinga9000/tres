from typing import override

from card import Card
from card.color import ALL_COLORS, CardColor
from . import Game
from views.argbuilder import ArgBuilder


class WildDrawCard(Card):
    def __init__(self, n: int):
        assert n >= 0
        super().__init__(ALL_COLORS, 50, 0, f"wild_draw_{n}", True)
        self.display_name = f"Wild Draw {n}"
        self.n = n
    
    @property
    @override
    def args(self):
        return ArgBuilder[Game]().add_color().with_callback(self.on_play)
    
    def on_play(self, game: Game, color: CardColor):
        self.color = color
        self.display_name = f'{self.color_name()} {self.display_name}'
        game.card_debt += self.n
