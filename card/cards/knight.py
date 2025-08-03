from typing import override
from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder
import random

class Knight(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, f"knight", False)

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        for p in game.players:
            if len(p.hand) >= 8:
                for _ in range(len(p.hand)//2):
                    p.hand.remove_card(random.choice(p.hand.cards))
