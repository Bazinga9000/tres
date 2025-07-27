from card import Card
import uuid

# A collection of cards in a Player's hand
class Hand():
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

    # todo: sort on display
    def display_all_cards(self) -> str:
        return "\n".join(i.display_name for i in self.cards)

    def __iter__(self):
        return self.cards.__iter__()
