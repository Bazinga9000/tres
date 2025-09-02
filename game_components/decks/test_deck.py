from .fixed_shoe import FixedShoe
from card import Card, CardColor
import card.cards as cards

from typing import TYPE_CHECKING, Any

# TODO: this probably shouldn't be with the deck infrastructure
if TYPE_CHECKING:
    from game import Game
else:
    Game = Any

def make_test_deck() -> list[Card[Game]]:
    out: list[Card[Game]] = []

    for c in [CardColor.RED, CardColor.ORANGE, CardColor.YELLOW, CardColor.GREEN, CardColor.BLUE, CardColor.PURPLE]:
        for _ in range(4):
            for n in range(0,16):
                out.append(cards.number_card(n)(c)) # Number cards
        for _ in range(3):
            out.append(cards.reverse_skip_draw(draws=2)(c))               # Draw 2s
            out.append(cards.reverse_skip_draw(reverse=True)(c))          # Reverse
            out.append(cards.reverse_skip_draw(skips=1)(c))               # Single Skip
            out.append(cards.reverse_skip_draw(reverse=True, skips=1)(c)) # Reverse Skip
        for _ in range(2):
            out.append(cards.reverse_skip_draw(draws=4)(c))                        # Draw 4
            out.append(cards.reverse_skip_draw(skips=2)(c))                        # Double Skip
            out.append(cards.reverse_skip_draw(reverse=True, draws=2)(c))          # Reverse Draw 2
            out.append(cards.reverse_skip_draw(skips=1, draws=2)(c))               # Skip Draw 2
            out.append(cards.reverse_skip_draw(reverse=True, skips=1, draws=2)(c)) # Reverse Skip Draw 2
            out.append(cards.revelation(c))                                    # Revelation
            out.append(cards.color_void(c))                                    # Color Void
            out.append(cards.pot_of_greed_n(2)(c))                             # Pot of Greed
        #out.append(cards.hand_swap(c))        # Hand Swap
        #out.append(cards.seat_swap(c))        # Seat Swap
        out.append(cards.hand_rotate(c))      # Hand Rotate
        #out.append(cards.wild_number(c))      # Wild Number
        #out.append(cards.kissaroo(c))         # Kissaroo
        out.append(cards.metadraw(c))         # Metadraw
        out.append(cards.pile_shuffle(c))     # Pile Shuffle
        out.append(cards.draw_times(2)(c))    # Draw 2x
        out.append(cards.knight(c))           # Knight
        out.append(cards.oopsie_daisy(c))     # Oopsie Daisy

    # Cards with fixed colors
    # for _ in range(6):
    #     out.append(cards.wild_draw_card(4))      # Wild Draw 4
    #     out.append(cards.wild_color_magnet())
    # for _ in range(15):
    #     out.append(cards.wild_card())            # Wild Cards
    out.append(cards.red_40())                   # Red 40
    #out.append(cards.dead_weight())              # Dead Weight

    return out

class TestDeck(FixedShoe[Game]):
    def __init__(self):
        super().__init__(make_test_deck)
