from typing import override
from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder


class DrawTimes(Card):
    def __init__(self, color: CardColor, n: int):
        assert n >= 1
        super().__init__(color, 30, 0, f"draw_times_{n}", True)
        self.display_name = f"{self.color_name()} Draw {n}x"
        self.n = n

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        game.card_debt *= self.n
