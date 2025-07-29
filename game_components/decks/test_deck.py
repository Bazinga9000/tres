from .fixed_shoe import FixedShoe
import card

def make_test_deck() -> list[card.Card]:
    out: list[card.Card] = []

    for c in [card.CardColor.RED, card.CardColor.ORANGE, card.CardColor.YELLOW, card.CardColor.GREEN, card.CardColor.BLUE, card.CardColor.PURPLE]:
        for n in range(1,16):
            out.append(card.NumberCard(c,n))
        for _ in range(2):
            out.append(card.DrawCard(c, 2))     # Draw 2s
            out.append(card.ReverseCard(c))     # Reverse
            out.append(card.SkipCard(c))        # Single Skip
            out.append(card.ReverseSkipCard(c)) # Reverse Skip
        out.append(card.HandSwap(c))        # Hand Swap
        out.append(card.SeatSwap(c))        # Seat Swap
        out.append(card.HandRotate(c))      # Hand Rotate

    # Cards with fixed colors
    for _ in range(2):
        out.append(card.WildDrawCard(4))        # Wild Draw 4
    for _ in range(5):
        out.append(card.WildCard())             # Wild Cards
    out.append(card.Red40())                    # Red 40

    return out

class TestDeck(FixedShoe):
    def __init__(self):
        super().__init__(make_test_deck)
