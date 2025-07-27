from card.abc import Card
from card.color import CardColor
from card.cards.number_card import NumberCard
from card.cards.basic_draw_card import DrawCard
from card.cards.reverse_card import ReverseCard
from card.cards.skip_card import SkipCard
from card.cards.reverse_skip import ReverseSkipCard
from card.cards.wild_card import WildCard, WildDrawCard

# Empty lambda to produce multiple copies of red 40
Red40 = lambda: NumberCard(CardColor.RED, 40)

__all__ = [
    'Card',
    'NumberCard',
    'DrawCard',
    'ReverseCard',
    'SkipCard',
    'ReverseSkipCard',
    'WildCard', 'WildDrawCard',
    'Red40'
]
