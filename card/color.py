from enum import Flag, auto

class CardColor(Flag):
    RED = auto()
    ORANGE = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()
    PURPLE = auto()

    @property
    def display_name(self) -> str:
        '''
        Print the name of this color.
        '''
        color_names = {
            CardColor.RED: "Red",
            CardColor.ORANGE: "Orange",
            CardColor.YELLOW: "Yellow",
            CardColor.GREEN: "Green",
            CardColor.BLUE: "Blue",
            CardColor.PURPLE: "Purple"
        }

        if self == NO_COLORS:
            return "Devoid" # todo: decide what to call this
        if self == ALL_COLORS:
            return "Rainbow" # todo: decide what to call THIS
        else:
            return "/".join(v for (k,v) in color_names.items() if k in self)

    @property
    def article(self) -> str:
        '''
        Returns the definite or indefinite article to use with this color.
        '''
        return "an" if self.display_name[0].lower() in "aeiou" else "a"

NO_COLORS = CardColor(0)
ALL_COLORS = CardColor.RED | CardColor.ORANGE | CardColor.YELLOW | CardColor.GREEN | CardColor.BLUE | CardColor.PURPLE
