import card.abc
from card.color import CardColor

class NumberCard(card.abc.Card):
    def __init__(self, color: CardColor, n: int):
        super().__init__(color, n, n, str(n))
