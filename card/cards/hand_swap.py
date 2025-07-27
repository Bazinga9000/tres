from typing import override
from card import Card
from card.color import CardColor
from game_components import Player
from views.cardview import CardView
from views.varview import VarView

class HandSwap(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, f"hand_swap", False)

    @override
    def on_select(self, view: CardView):
        def on_play(p: Player):
            p.hand, view.game.active_player.hand = view.game.active_player.hand, p.hand
        return VarView(view).add_player(skip_self=True).add_callback(on_play)
