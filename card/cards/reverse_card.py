from typing import override

from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder


class ReverseCard(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 20, 0, "reverse", False)
    
    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)
    
    def on_play(self, game: Game):
        game.players = game.players[::-1]
        game.whose_turn = len(game.players) - game.whose_turn - 1
