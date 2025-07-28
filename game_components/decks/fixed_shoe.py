from collections.abc import Callable
from typing import TYPE_CHECKING, Any, override
from .abc import Deck
import random
if TYPE_CHECKING:
    from card import Card
else:
    Card = Any


'''
A deck generates a fixed list of cards (the "shoe") each time it runs out.
Used for more "classical" Tres decks.

The function passed to __init__ does not need to shuffle, the deck itself handles that.
'''
class FixedShoe(Deck):
    def __init__(self, generator: Callable[[], list[Card]]):
        self.get_new_shoe = generator
        self.refresh_shoe()
        assert self.shoe != []

    def refresh_shoe(self):
        self.shoe : list[Card] = self.get_new_shoe()
        random.shuffle(self.shoe)

    @override
    def draw_from_deck(self) -> Card:
        if self.shoe == []:
            self.refresh_shoe()

        return self.shoe.pop()

    @override
    def place_on_top(self, card: Card):
        self.shoe.append(card)
