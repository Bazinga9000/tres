from typing import override
from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder
import util.number_names


class ReverseSkipDraw(Card):
    def __init__(self, color: CardColor, *, reverse: bool=False, draw: int=0, skip: int=0):
        assert draw >= 0 and skip >= 0
        assert reverse or draw > 0 or skip > 0
        self.r = reverse
        self.s = skip
        self.d = draw

        card_types: list[str] = []
        card_name: list[str] = []
        if self.r:
            card_types.append("reverse")
            card_name.append("Reverse")
        if self.s > 0:
            card_types.append(f"skip_{self.s}")
            if self.s > 1:
                card_name.append(util.number_names.tuple_name(self.s))
            card_name.append("Skip")
        if self.d > 0:
            card_types.append(f"draw_{self.d}")
            card_name.append(f"Draw {self.d}")

        super().__init__(color, 30, 0, "_".join(card_types), (self.d > 0))
        self.display_name = f"{self.color_name()} {' '.join(card_name)}"

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        if self.r:
            game.table.reverse_direction()

        if self.s > 0:
            game.table.skip(self.s)

        if self.d > 0:
            game.card_debt += self.d
