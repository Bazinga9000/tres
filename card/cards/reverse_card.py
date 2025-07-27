from typing import override

from card import Card
from card.color import CardColor
from views.cardview import CardView
from views.varview import VarView

class ReverseCard(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 20, 0, "reverse", False)

    @override
    def on_select(self, view: CardView):
        def on_play():
            view.game.players = view.game.players[::-1]
            view.game.whose_turn = len(view.game.players) - view.game.whose_turn - 1
        return VarView(view).add_callback(on_play)
