from card.abc import Card
from card.color import CardColor
from card.cards.number_card import NumberCard
from card.cards.basic_draw_card import DrawCard
from card.cards.reverse_card import ReverseCard
from card.cards.skip_card import SkipCard
from card.cards.reverse_skip import ReverseSkipCard
from card.cards.wild_card import WildCard
from card.cards.wild_draw_card import WildDrawCard
from card.cards.hand_swap import HandSwap
from card.cards.seat_swap import SeatSwap
from card.cards.hand_rotate import HandRotate
from card.cards.wild_number import WildNumber

# Empty lambda to produce multiple copies of red 40
Red40 = lambda: NumberCard(CardColor.RED, 40)

# Dead Weight
DeadWeight = lambda: Card(CardColor.ORANGE, -50, 0, "dead_weight", False)

__all__ = [
    'Card',
    'NumberCard',
    'DrawCard',
    'ReverseCard',
    'SkipCard',
    'ReverseSkipCard',
    'WildCard',
    'WildDrawCard',
    'Red40',
    'HandSwap',
    'SeatSwap',
    'HandRotate',
    'WildNumber',
    'DeadWeight'
]
