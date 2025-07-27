from typing import Mapping, override

from card import Card
from card.args import CardArg
from card.color import CardColor
from card.abc import Game
from views.cardview import CardView
from views.varview import VarView


class ReverseSkipCard(Card):
    def __init__(self, color: CardColor, n: int=1):
        assert n >= 1
        super().__init__(color, 20, 0, f"reverse_skip_{n}", False)
        cn = self.color_name()
        self.display_name = f"{cn} Reverse Skip {n}" if n > 1 else f"{cn} Reverse Skip"
        self.n = n

    @override
    def on_play(self, game: Game, pile_index: int, card_args: Mapping[str, CardArg]):
        game.players = game.players[::-1]
        game.whose_turn = len(game.players) - game.whose_turn - 1
        game.whose_turn = (game.whose_turn + self.n)%len(game.players)
    
    @override
    def on_select(self, view: CardView):
        def on_play():
            view.game.players = view.game.players[::-1]
            view.game.whose_turn = len(view.game.players) - view.game.whose_turn - 1
            view.game.whose_turn = (view.game.whose_turn + self.n) % len(view.game.players)
        return VarView(view).add_callback(on_play)
