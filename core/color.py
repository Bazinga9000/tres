from enum import Flag, auto


class CardColor(Flag):
    RED = auto()
    ORANGE = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()
    PURPLE = auto()
    DEVOID = 0
    RAINBOW = RED | ORANGE | YELLOW | GREEN | BLUE | PURPLE
    
    @property
    def name(self) -> str:
        return (super().name or 'Unobtanium').title()
    
    @property
    def article(self) -> str:
        '''
        Returns the definite or indefinite article to use with this color.
        '''
        return "an" if self.name[0].lower() in "aeiou" else "a"
