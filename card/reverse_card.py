from typing import Any, override

import card.abc
from card.color import CardColor

class ReverseCard(card.abc.Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 20, 0, "reverse", False)

    @override
    def on_play(self, game: card.abc.Game, pile_index: int, card_args: dict[str, list[Any]]):
        game.players = game.players[::-1]
        game.whose_turn = len(game.players) - game.whose_turn - 1
