from typing import Mapping, override
from card import Card
from card.args import CardArg
from card.color import CardColor
from card.abc import Game
from cap.cardview import CardView
from cap.varview import VarView

class DrawCard(Card):
    def __init__(self, color: CardColor, n: int):
        assert n >= 1
        super().__init__(color, 30, 0, f"draw_{n}", True)
        self.display_name = f"{self.color_name()} Draw {n}"
        self.n = n

    @override
    def on_play(self, game: Game, pile_index: int, card_args: Mapping[str, CardArg]):
        game.card_debt += self.n
    
    @override
    def on_select(self, view: CardView):
        def on_play():
            view.game.card_debt += self.n
        return VarView(view).add_callback(on_play)
