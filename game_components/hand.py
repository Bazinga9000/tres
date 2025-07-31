import uuid
from typing import TYPE_CHECKING, Any
from PIL import Image

# yet another circular dependency
if TYPE_CHECKING:
    from card import Card
else:
    Card = Any

# A collection of cards in a Player's hand
class Hand:
    def __init__(self):
        self.cards : list[Card] = []

    def __len__(self) -> int:
        return len(self.cards)

    def add_card(self, c: Card):
        self.cards.append(c)

    def lookup_card(self, u: uuid.UUID) -> Card | None:
        for c in self.cards:
            if c.uuid == u:
                return c
        return None

    def remove_card(self, c: Card):
        self.cards.remove(c)

    def sorted(self) -> list[Card]:
        out : list[Card] = self.cards[:]
        return sorted(out, key=lambda x: x.sort_key())

    def display_all_cards(self) -> str:
        return "\n".join(i.display_name for i in self.sorted())

    def render_all_cards(self) -> list[Image.Image]:
        return [i.render() for i in self.sorted()]

    def __iter__(self):
        return self.cards.__iter__()
