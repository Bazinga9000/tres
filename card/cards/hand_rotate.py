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
        non_ejected_players = [p for p in game.table.starting_with_you]
        hands = [p.hand for p in non_ejected_players]
        hands.insert(0, hands.pop())
        for i in range(len(non_ejected_players)):
            non_ejected_players[i].hand = hands[i]
