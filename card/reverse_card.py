import card.abc
from card.color import CardColor

class ReverseCard(card.abc.Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 20, 0, "reverse", False)

    def on_play(self, game, pile_index : int, card_args):
        game.players = game.players[::-1]
        game.whose_turn = len(game.players) - game.whose_turn - 1
        pass
