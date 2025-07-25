import card.abc
from card.color import CardColor

class DrawCard(card.abc.Card):
    def __init__(self, color: CardColor, n: int):
        assert n >= 1
        super().__init__(color, 30, 0, f"draw_{n}", True)
        self.display_name = f"{self.color_name()} Draw {n}"
        self.n = n

    def on_play(self, game, pile_index, card_args):
        game.card_debt += self.n
