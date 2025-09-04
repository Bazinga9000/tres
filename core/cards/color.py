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

        if self == self.devoid():
            return "Devoid" # TODO: decide what to call this
        if self == self.rainbow():
            return "Rainbow" # TODO: decide what to call THIS
        else:
            return "/".join(v for (k,v) in color_names.items() if k in self)

    @property
    def article(self) -> str:
        '''
        Returns the definite or indefinite article to use with this color.
        '''
        return "an" if self.display_name[0].lower() in "aeiou" else "a"
    
    @classmethod
    def devoid(cls):
        return cls(0)
    
    @classmethod
    def rainbow(cls):
        return cls.RED | cls.ORANGE | cls.YELLOW | cls.GREEN | cls.BLUE | cls.PURPLE
