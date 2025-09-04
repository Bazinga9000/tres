from enum import Flag, auto
from typing import override


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
    @override
    def name(self) -> str:
        return (super().name or 'Unobtanium').title()
    
    @property
    def article(self) -> str:
        '''
        Returns the indefinite article to use with this color.
        '''
        return "an" if self.name[0].lower() in "aeiou" else "a"
