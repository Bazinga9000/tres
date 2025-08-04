from typing import override
from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder
import random

class OopsieDaisy(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, f"oopsie_daisy", False)

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        hand_sizes: list[int] = []
        all_cards: list[Card] = []
        for p in game.players:
            hand_sizes.append(len(p.hand))
            all_cards.extend(p.hand)
            p.hand.cards = []
        random.shuffle(all_cards)
        for n,p in enumerate(game.players):
            for _ in range(n):
                p.hand.add_card(all_cards.pop())
