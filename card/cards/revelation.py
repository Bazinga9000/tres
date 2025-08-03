from card import Card, CardColor


# the meat of this is in hand.is_revealed()
class Revelation(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 20, 0, "revelation", False)
