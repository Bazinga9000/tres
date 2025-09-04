import abc

from .card import Card


class Deck[T](abc.ABC):
    type Card = Card[T]

    @abc.abstractmethod
    def draw_from_deck(self) -> Card:
        """
        Draw a card from this deck. Should return a unique card (different UUID) every call.
        Decks in Tres should never run out.
        This method should respect place_on_top
        """
        pass

    @abc.abstractmethod
    def place_on_top(self, card: Card):
       """
       Place a card on top of the deck.
       """
       pass
