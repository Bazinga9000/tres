from typing import Any, override
import card.abc
from card.color import *
from card.card_arg import *

class WildCard(card.abc.Card):
    def __init__(self):
        super().__init__(ALL_COLORS, 50, 0, "wild", False)
        self.display_name = "Wild"

    @override
    def on_play(self, game: card.abc.Game, pile_index: int, card_args: dict[str, list[Any]]):
        self.color = card_args["color"][0]
        self.display_name = f"{self.color_name()} {self.display_name}"

    def get_args(self):
        return {
            "color": CardArg(CardArgType.Color, "Select the color for this card to become...")
        }

# todo: split this off after we pull out common functionality
class WildDrawCard(WildCard):
    def __init__(self, n: int):
        assert n >= 1
        super().__init__()
        self.display_name += f" Draw {n}"
        self.n = n
        self.type = f"wild_draw_{n}"

    @override
    def on_play(self, game: card.abc.Game, pile_index: int, card_args: dict[str, list[Any]]):
        super().on_play(game, pile_index, card_args)
        game.card_debt += self.n
