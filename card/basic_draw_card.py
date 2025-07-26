from typing import Any, override
import card.abc
from card.color import CardColor

class DrawCard(card.abc.Card):
    def __init__(self, color: CardColor, n: int):
        assert n >= 1
        super().__init__(color, 30, 0, f"draw_{n}", True)
        self.display_name = f"{self.color_name()} Draw {n}"
        self.n = n

    @override
    def on_play(self, game: card.abc.Game, pile_index: int, card_args: dict[str, list[Any]]):
        game.card_debt += self.n
