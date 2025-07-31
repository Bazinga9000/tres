from typing import override

from card import Card
from card.color import CardColor
from util.number_names import tuple_name
from . import Game
from views.argbuilder import ArgBuilder


class SkipCard(Card):
    def __init__(self, color: CardColor, n: int=1):
        assert n >= 1
        super().__init__(color, 20, 0, f"skip_{n}", False)
        cn = self.color_name()
        self.display_name = f"{cn} {tuple_name(n)} Skip" if n > 1 else f"{cn} Skip"
        self.n = n

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        game.whose_turn += self.n
        game.whose_turn %= len(game.players)
