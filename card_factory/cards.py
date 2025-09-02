import util.number_names
import random

from .factory import CardFactory, card
from .color import CardColor
from .abc import Card
from game import Game

def number_card(n: int) -> CardFactory[Game]:
    @card(
        default_penalty_points = n,
        default_number_value = n,
        default_card_type = str(n),
    )
    def factory(game: Game):
        pass
    return factory

red_40_factory = number_card(40)
red_40 = lambda: red_40_factory(CardColor.RED)

@card(
    default_penalty_points = 30,
)
def color_void(game: Game):
    me = game.piles[game.active_pile].pop()
    for card in [c for c in game.active_player.hand if bool(c.color & me.color)]:
        game.active_player.hand.remove_card(card)
        game.piles[game.active_pile].append(card)
    game.piles[game.active_pile].append(me)

def draw_times(n: int):
    assert n >= 1
    @card(
        default_penalty_points = 30,
        default_card_type = f"draw_times_{n}",
        default_raw_name = f"%c Draw {n}×",
        default_debtstackable = True
    )
    def factory(game: Game):
        game.card_debt *= n
    return factory

@card(
    default_penalty_points = 30,
)
def hand_rotate(game: Game):
    non_ejected_players = [p for p in game.table.starting_with_you]
    hands = [p.hand for p in non_ejected_players]
    hands.insert(0, hands.pop())
    for i in range(len(non_ejected_players)):
        non_ejected_players[i].hand = hands[i]

# todo: NEEDS ARGBUILDER
'''
class HandSwap(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, "hand_swap", False)

    @property
    @override
    def args(self):
        return ArgBuilder[Game]().add_player(skip_self=True).with_callback(self.on_play)

    def on_play(self, game: Game, player: Player):
        player.hand, game.active_player.hand = game.active_player.hand, player.hand


class Kissaroo(Card):
    def __init__(self, c: CardColor):
        super().__init__(c, 50, 0, "kissaroo", False)
        if self.color_name()[0].lower() in ["a","e","i","o","u"]:
            article = "An"
        else:
            article = "A"

        self.display_name = f"{article} {self.color_name()} Kissaroo from Me to You"

    @property
    @override
    def args(self):
        return ArgBuilder[Game]().add_card(requires_playable=False).add_player(skip_self=True).with_callback(self.on_play)

    def on_play(self, game: Game, card: Card, target: Player):
        game.active_player.hand.remove_card(card)
        target.hand.add_card(card)
'''

@card(
    default_penalty_points = 30,
)
def knight(game: Game):
    for p in game.table.starting_with_you:
        if len(p.hand) >= 8:
            for _ in range(len(p.hand)//2):
                p.hand.remove_card(random.choice(p.hand.cards))

@card(
    default_penalty_points = 30,
)
def metadraw(game: Game):
    top_card = game.piles[game.active_pile][-2] # [-1] is always this card
    game.card_debt += top_card.number_value

@card(
    default_penalty_points = 30,
)
def oopsie_daisy(game: Game):
    hand_sizes: list[int] = []
    all_cards: list[Card[Game]] = []
    for p in game.table.starting_with_you:
        hand_sizes.append(len(p.hand))
        all_cards.extend(p.hand)
        p.hand.cards = []
    random.shuffle(all_cards)
    for n,p in enumerate(game.table.starting_with_you):
        for _ in range(n):
            p.hand.add_card(all_cards.pop())

@card(
    default_penalty_points = 5,
)
def pile_shuffle(game: Game):
    random.shuffle(game.piles[game.active_pile])

def pot_of_greed_n(draws: int):
    assert draws >= 0
    card_type = "pot_of_greed" + ("" if draws == 2 else f"_{draws}")
    card_name = f"%C {("" if draws == 2 else util.number_names.tuple_name(draws) + " ")}Pot of Greed"

    @card(
        default_penalty_points = 30,
        default_card_type = card_type,
        default_raw_name = card_name
    )
    def factory(game: Game):
        for _ in range(draws):
            game.active_player.hand.add_card(game.deck.draw_from_deck())
    return factory

@card(
    default_penalty_points = 20
)
def revelation(game: Game):
    pass # the meat of this is in hand.is_revealed()

def reverse_skip_draw(reverse: bool, skips: int, draws: int) -> CardFactory[Game]:
    assert draws >= 0 and skips >= 0
    assert reverse or draws > 0 or skips > 0

    card_types: list[str] = []
    card_name: list[str] = ["%C"]
    if reverse:
        card_types.append("reverse")
        card_name.append("Reverse")
    if skips > 0:
        card_types.append(f"skip_{skips}")
        if skips > 1:
            card_name.append(util.number_names.tuple_name(skips))
        card_name.append("Skip")
    if draws > 0:
        card_types.append(f"draw_{draws}")
        card_name.append(f"Draw {draws}")

    @card(
        default_penalty_points = 30,
        default_card_type = "_".join(card_types),
        default_raw_name = " ".join(card_name),
        default_debtstackable = draws > 0,
    )
    def factory(game: Game):
        if reverse:
            game.table.reverse_direction()

        if skips > 0:
            game.table.skip(skips)

        if draws > 0:
            game.card_debt += draws

    return factory

# TODO: REQUIRES ARGBUILDER
'''
class SeatSwap(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, "seat_swap", False)

    @property
    @override
    def args(self):
        return ArgBuilder[Game]().add_player(skip_self=True).with_callback(self.on_play)

    def on_play(self, game: Game, player: Player):
        game.table.swap_players(game.table.active_player, player)
'''

def apply_wild(card: Card[Game], color: CardColor):
    '''
    Utility method to update a color changing card's color.
    This will also add %C to the raw name if it is not already present.
    '''
    card.color = color
    if "%C" not in card.raw_name:
        card.raw_name = "%C " + card.raw_name


# TODO: all wild X cards require argbuilder, but i've done a bit of the work here already
'''
@constant_color(ALL_COLORS)
@card(
    default_penalty_points = 50,
    default_raw_name = "Wild"
)
def wild(self: Card[Game], game: Game, color: CardColor):
    apply_wild(self, color)

@constant_color(ALL_COLORS)
@card(
    default_penalty_points = 50,
    default_raw_name = "Wild Color Magnet"
)
def wild_color_magnet(self: Card[Game], game: Game, color: CardColor):
    apply_wild(self, color)
    next = game.table.next_player
    while True:
        c = game.deck.draw_from_deck()
        next.hand.add_card(c)

        if c.color == self.color: # todo: should this be an exact match?
            break

def wild_draw_n(n: int):
    assert n >= 0
    @constant_color(ALL_COLORS)
    @card(
        default_penalty_points = 50,
        default_card_type = f"wild_draw_{n}",
        default_raw_name = f"Wild Draw {n}"
    )
    def factory(self: Card[Game], game: Game, color: CardColor):
        apply_wild(self, color)
        game.card_debt += n
    return factory

@card(
    default_penalty_points = 50,
)
def wild_number(self: Card[Game], game: Game, n: int):
    self.card_type = str(n)
    self.number_value = n
    self.display_name = f'{self.display_name} ({n})'
'''
