from enum import Flag, auto

class CardColor(Flag):
    RED = auto()
    ORANGE = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()
    PURPLE = auto()


NO_COLORS = CardColor(0)
ALL_COLORS = CardColor.RED | CardColor.ORANGE | CardColor.YELLOW | CardColor.GREEN | CardColor.BLUE | CardColor.PURPLE
