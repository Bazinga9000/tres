from card.abc import Card
from card.color import CardColor
from card.cards.number_card import NumberCard
from card.cards.reverse_skip_draw import ReverseSkipDraw
from card.cards.wild_card import WildCard
from card.cards.wild_draw_card import WildDrawCard
from card.cards.hand_swap import HandSwap
from card.cards.seat_swap import SeatSwap
from card.cards.hand_rotate import HandRotate
from card.cards.wild_number import WildNumber
from card.cards.kissaroo import Kissaroo
from card.cards.metadraw import MetaDraw
from card.cards.pile_shuffle import PileShuffle
from card.cards.draw_times import DrawTimes
from card.cards.knight import Knight
from card.cards.revelation import Revelation
from card.cards.oopsie_daisy import OopsieDaisy

# Empty lambda to produce multiple copies of red 40
Red40 = lambda: NumberCard(CardColor.RED, 40)

# Dead Weight
DeadWeight = lambda: Card(CardColor.ORANGE, -50, 0, "dead_weight", False)

__all__ = [
    'Card',
    'NumberCard',
    'ReverseSkipDraw',
    'WildCard',
    'WildDrawCard',
    'Red40',
    'HandSwap',
    'SeatSwap',
    'HandRotate',
    'WildNumber',
    'DeadWeight',
    'Kissaroo',
    'MetaDraw',
    'PileShuffle',
    'DrawTimes',
    'Knight',
    'Revelation',
    'OopsieDaisy'
]
