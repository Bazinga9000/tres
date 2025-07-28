from card import Card, CardColor


class NumberCard(Card):
    def __init__(self, color: CardColor, n: int):
        super().__init__(color, n, n, str(n), False)
