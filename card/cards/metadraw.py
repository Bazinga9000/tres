from typing import override
from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder


class MetaDraw(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, f"metadraw", True)

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        top_card = game.piles[game.active_pile][-2] # [-1] is always this card
        game.card_debt += top_card.number_value
