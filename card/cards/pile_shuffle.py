from typing import override
from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder
import random

class PileShuffle(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 5, 0, "pile_shuffle", False)

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        random.shuffle(game.piles[game.active_pile])
