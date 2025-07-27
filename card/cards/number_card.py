from typing import override
import card.abc
from card.color import CardColor
from cap.cardview import CardView
from cap.varview import VarView

class NumberCard(card.abc.Card):
    def __init__(self, color: CardColor, n: int):
        super().__init__(color, n, n, str(n), False)
    
    @override
    def on_select(self, view: CardView):
        def on_play():
            pass
        return VarView(view).add_callback(on_play)
