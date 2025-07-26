from typing import Any, override
import card.abc
from card.color import CardColor


class SkipCard(card.abc.Card):
    def __init__(self, color: CardColor, n: int=1):
        assert n >= 1
        super().__init__(color, 20, 0, f"skip_{n}", False)
        cn = self.color_name()
        self.display_name = f"{cn} Skip {n}" if n > 1 else f"{cn} Skip"
        self.n = n

    @override
    def on_play(self, game: card.abc.Game, pile_index: int, card_args: dict[str, list[Any]]):
        game.whose_turn = (game.whose_turn + self.n)%len(game.players)
