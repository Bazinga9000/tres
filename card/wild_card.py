from typing import Mapping, override

from card import Card
from card.args import CardArg, ColorArg
from card.color import ALL_COLORS
from card.abc import Game

class WildCard(Card):
    def __init__(self):
        super().__init__(ALL_COLORS, 50, 0, "wild", False)
        self.display_name = "Wild"

    @override
    def on_play(self, game: Game, pile_index: int, card_args: Mapping[str, CardArg]):
        assert card_args["color"].is_populated()
        # todo: this second assert only exists to make the type checker happy
        # even though it is already checked in the previous assert
        # figure out a way to make this not necessary
        assert card_args["color"].values is not None
        self.color = card_args["color"].values[0]
        self.display_name = f"{self.color_name()} {self.display_name}"

    def get_args(self):
        return {
            "color": ColorArg(self, "Select the color for this card to become...")
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
    def on_play(self, game: Game, pile_index: int, card_args: Mapping[str, CardArg]):
        super().on_play(game, pile_index, card_args)
        game.card_debt += self.n
