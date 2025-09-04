import random

from .args import choose_card, choose_color, choose_player
from .card import card
from core.cards import Card, CardColor
from core.players.player import Player
from game import Game
from util.decorators import decorates
from util.number_names import tuple_name

from typeutils import F


# TODO: split these up into multiple files

def number_card(n: int):
    return card(
        penalty = n,
        number_value = n,
        card_type = str(n),
    )(lambda g: None) # no on_play effect

red_40 = lambda: number_card(40)(CardColor.RED)

@card(
    penalty=30,
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
        penalty=30,
        card_type=f"draw_times_{n}",
        raw_name=f"%c Draw {n}×",
        can_play_on_debt=True
    )
    def factory(game: Game):
        game.card_debt *= n
    return factory

@card(
    penalty=30,
)
def hand_rotate(game: Game):
    non_ejected_players = [p for p in game.table.starting_with_you]
    hands = [p.hand for p in non_ejected_players]
    hands.insert(0, hands.pop())
    for i in range(len(non_ejected_players)):
        non_ejected_players[i].hand = hands[i]

@card(
    penalty=30,
)
@choose_player(skip_self=True)
def hand_swap(game: Game, target: Player[Game]): # TODO: type Player = Player[Game]?
    game.active_player.hand, target.hand = target.hand, game.active_player.hand


@card(
    penalty=50
)
@choose_player(skip_self=False) # TODO: set to true - this is just for testing
@choose_card(requires_playable=False)
def kissaroo(game: Game, target: Player[Game], card: Card[Game]):
    # TODO: display name doesn't work here
    game.active_player.hand.remove_card(card)
    target.hand.add_card(card)


@card(
    penalty=30,
)
def knight(game: Game):
    for p in game.table.starting_with_you:
        if len(p.hand) >= 8:
            for _ in range(len(p.hand)//2):
                p.hand.remove_card(random.choice(p.hand.cards))

@card(
    penalty=30,
)
def metadraw(game: Game):
    top_card = game.piles[game.active_pile][-2] # [-1] is always this card
    game.card_debt += top_card.number_value

@card(
    penalty=30,
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
    penalty=5,
)
def pile_shuffle(game: Game):
    random.shuffle(game.piles[game.active_pile])

def pot_of_greed_n(draws: int):
    assert draws >= 0
    card_type = "pot_of_greed" + ("" if draws == 2 else f"_{draws}")
    card_name = f"%C {("" if draws == 2 else tuple_name(draws) + " ")}Pot of Greed"

    @card(
        penalty=30,
        card_type=card_type,
        raw_name=card_name
    )
    def on_play(game: Game):
        for _ in range(draws):
            game.active_player.hand.add_card(game.deck.draw_from_deck())
    return on_play

@card(
    penalty=20
)
def revelation(game: Game):
    pass # the meat of this is in hand.is_revealed()

def reverse_skip_draw(*, reverse: bool = False, skips: int = 0, draws: int = 0):
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
            card_name.append(tuple_name(skips))
        card_name.append("Skip")
    if draws > 0:
        card_types.append(f"draw_{draws}")
        card_name.append(f"Draw {draws}")

    @card(
        penalty=30,
        card_type="_".join(card_types),
        raw_name=" ".join(card_name),
        can_play_on_debt=draws > 0,
    )
    def on_play(game: Game):
        if reverse:
            game.table.reverse_direction()

        if skips > 0:
            game.table.skip(skips)

        if draws > 0:
            game.card_debt += draws

    return on_play


@card(
    penalty=30,
)
@choose_player(skip_self=True)
def seat_swap(game: Game, target: Player[Game]):
    game.table.swap_players(game.table.active_player, target)


def apply_wild(game: Game, color: CardColor):
    '''
    Utility method to update a color changing card's color.
    This will also add %C to the raw name if it is not already present.
    '''
    card = game.piles[game.active_pile][-1]
    card.color = color
    if "%C" not in card.raw_name:
        card.raw_name = "%C " + card.raw_name


def constant_color(color: CardColor):
    @decorates
    def wrapper(fun: F[[CardColor], Card[Game]]):
        return fun(color)
    return wrapper

@constant_color(CardColor.rainbow())
@card(
    penalty=50,
    raw_name="Wild"
)
@choose_color()
def wild(game: Game, color: CardColor):
    apply_wild(game, color)


@constant_color(CardColor.rainbow())
@card(
    penalty = 50,
    raw_name = "Wild Color Magnet"
)
@choose_color()
def wild_color_magnet(game: Game, color: CardColor):
    apply_wild(game, color)
    next = game.table.next_player
    while True:
        c = game.deck.draw_from_deck()
        next.hand.add_card(c)

        if c.color == color: # TODO: should this be an exact match?
            break

def wild_draw_n(n: int):
    assert n >= 0
    @constant_color(CardColor.rainbow())
    @card(
        penalty = 50,
        card_type = f"wild_draw_{n}",
        raw_name = f"Wild Draw {n}"
    )
    @choose_color()
    def on_play(game: Game, color: CardColor):
        apply_wild(game, color)
        game.card_debt += n
    return on_play

def wild_number(n: int):
    @constant_color(CardColor.rainbow())
    @card(
        penalty = n,
        number_value = n,
        card_type = str(n),
    )
    @choose_color()
    def on_play(game: Game, color: CardColor):
        apply_wild(game, color)
    return on_play
