from typing import override

from card import Card
from card.color import ALL_COLORS, CardColor
from views.cardview import CardView
from views.varview import VarView

class WildCard(Card):
    def __init__(self):
        super().__init__(ALL_COLORS, 50, 0, "wild", False)
        self.display_name = "Wild"

    @override
    def on_select(self, view: CardView):
        def on_play(color: CardColor):
            self.color = color
            self.display_name = f'{self.color_name()} {self.display_name}'
        return VarView(view).add_color().add_callback(on_play)


# todo: split this off after we pull out common functionality
class WildDrawCard(Card):
    def __init__(self, n: int):
        assert n >= 0
        super().__init__(ALL_COLORS, 50, 0, f"wild_draw_{n}", True)
        self.display_name = f"Wild Draw {n}"
        self.n = n

    @override
    def on_select(self, view: CardView):
        def on_play(color: CardColor):
            self.color = color
            self.display_name = f'{self.color_name()} {self.display_name}'
            view.game.card_debt += self.n
        return VarView(view).add_color().add_callback(on_play)
