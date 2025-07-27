from typing import Mapping, override

from card import Card
from card.args import CardArg
from card.color import CardColor
from card.abc import Game

class ReverseCard(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 20, 0, "reverse", False)

    @override
    def on_play(self, game: Game, pile_index: int, card_args: Mapping[str, CardArg]):
        game.players = game.players[::-1]
        game.whose_turn = len(game.players) - game.whose_turn - 1
