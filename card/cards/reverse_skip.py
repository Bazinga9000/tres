from typing import override

from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder


class ReverseSkipCard(Card):
    def __init__(self, color: CardColor, n: int=1):
        assert n >= 1
        super().__init__(color, 20, 0, f"reverse_skip_{n}", False)
        cn = self.color_name()
        self.display_name = f"{cn} Reverse Skip {n}" if n > 1 else f"{cn} Reverse Skip"
        self.n = n
    
    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)
    
    def on_play(self, game: Game):
        game.players = game.players[::-1]
        game.whose_turn = len(game.players) - game.whose_turn - 1
        game.whose_turn = (game.whose_turn + self.n) % len(game.players)
