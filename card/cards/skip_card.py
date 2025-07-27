from typing import override

from card import Card
from card.color import CardColor
from views.cardview import CardView
from views.varview import VarView


class SkipCard(Card):
    def __init__(self, color: CardColor, n: int=1):
        assert n >= 1
        super().__init__(color, 20, 0, f"skip_{n}", False)
        cn = self.color_name()
        self.display_name = f"{cn} Skip {n}" if n > 1 else f"{cn} Skip"
        self.n = n

    @override
    def on_select(self, view: CardView):
        def on_play():
            view.game.whose_turn = (view.game.whose_turn + self.n) % len(view.game.players)
        return VarView(view).add_callback(on_play)
