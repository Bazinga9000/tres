from typing import override

from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder


class HandRotate(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, "hand_rotate", False)

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        hands = [p.hand for p in game.players]
        hands.insert(0, hands.pop())
        for i in range(len(game.players)):
            game.players[i].hand = hands[i]
