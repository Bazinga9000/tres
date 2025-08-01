from .fixed_shoe import FixedShoe
import card

def make_test_deck() -> list[card.Card]:
    out: list[card.Card] = []

    for c in [card.CardColor.RED, card.CardColor.ORANGE, card.CardColor.YELLOW, card.CardColor.GREEN, card.CardColor.BLUE, card.CardColor.PURPLE]:
        for _ in range(4):
            for n in range(0,16):
                out.append(card.NumberCard(c,n))
        for _ in range(3):
            out.append(card.ReverseSkipDraw(c, draw=2))               # Draw 2s
            out.append(card.ReverseSkipDraw(c, reverse=True))         # Reverse
            out.append(card.ReverseSkipDraw(c, skip=1))               # Single Skip
            out.append(card.ReverseSkipDraw(c, reverse=True, skip=1)) # Reverse Skip
        for _ in range(2):
            out.append(card.ReverseSkipDraw(c, draw=4))                       # Draw 4
            out.append(card.ReverseSkipDraw(c, skip=2))                       # Double Skip
            out.append(card.ReverseSkipDraw(c, reverse=True, draw=2))         # Reverse Draw 2
            out.append(card.ReverseSkipDraw(c, skip=1, draw=2))               # Skip Draw 2
            out.append(card.ReverseSkipDraw(c, reverse=True, skip=1, draw=2)) # Reverse Skip Draw 2
        out.append(card.HandSwap(c))        # Hand Swap
        out.append(card.SeatSwap(c))        # Seat Swap
        out.append(card.HandRotate(c))      # Hand Rotate
        out.append(card.WildNumber(c))  # Wild Number
        out.append(card.Kissaroo(c))    # Kissaroo
        out.append(card.MetaDraw(c))    # Metadraw
        out.append(card.PileShuffle(c)) # Pile Shuffle
        out.append(card.DrawTimes(c, 2))# Draw 2x

    # Cards with fixed colors
    for _ in range(2):
        out.append(card.WildDrawCard(4))        # Wild Draw 4
    for _ in range(5):
        out.append(card.WildCard())             # Wild Cards
    out.append(card.Red40())                    # Red 40
    out.append(card.DeadWeight())               # Dead Weight

    return out

class TestDeck(FixedShoe):
    def __init__(self):
        super().__init__(make_test_deck)
