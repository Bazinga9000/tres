import random

from core import Card, Deck

from typing import override
from typeutils import Factory


class FixedShoe[T](Deck[T]):
    '''
    A deck generates a fixed list of cards (the "shoe") each time it runs out.
    Used for more "classical" Tres decks.

    The function passed to __init__ does not need to shuffle, the deck itself handles that.
    '''
    
    def __init__(self, generator: Factory[list[Card[T]]]):
        self.get_new_shoe = generator
        self.refresh_shoe()
        assert self.shoe != []
    
    def refresh_shoe(self):
        self.shoe = self.get_new_shoe()
        random.shuffle(self.shoe)
    
    @override
    def draw_from_deck(self) -> Card[T]:
        if self.shoe == []:
            self.refresh_shoe()
        
        return self.shoe.pop()
    
    @override
    def place_on_top(self, card: Card[T]):
        self.shoe.append(card)
