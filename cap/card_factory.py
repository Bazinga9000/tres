from dataclasses import dataclass, field
from enum import Flag, auto
from typing import Callable, Self
from uuid import UUID, uuid4
import util.number_names

from game_components import Player
from views.argbuilder import ArgBuilder, ArgBuilderBase

# TODO: copied from existing card color
class CardColor(Flag):
    RED = auto()
    ORANGE = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()
    PURPLE = auto()


NO_COLORS = CardColor(0)
ALL_COLORS = CardColor.RED | CardColor.ORANGE | CardColor.YELLOW | CardColor.GREEN | CardColor.BLUE | CardColor.PURPLE


# TODO: separate
from game import Game

@dataclass
class Card[T]:
    color: CardColor
    rules: str
    penalty_points: int
    number_value: int
    card_type: str
    can_play_on_debt: bool

    # hooks
    args: ArgBuilderBase[T]
    # todo: actually hook the hook
    card_draw_hook: Callable[[Self, Game, Player], None]

    # autogenerate UUID
    uuid: UUID = field(default_factory=uuid4)



@dataclass
class CardFactory[T]:
    default_color: CardColor
    default_rules: str
    default_penalty: int
    default_numerical_value: int
    default_type: str
    default_debtstackable: bool
    default_args: ArgBuilderBase[T]
    default_card_draw_hook: Callable[[Card[T], Game, Player], None] | None = None

    def __call__(self) -> Card[T]:
        return Card(
            color = self.default_color,
            rules = self.default_rules,
            penalty_points = self.default_penalty,
            number_value = self.default_numerical_value,
            card_type = self.default_type,
            can_play_on_debt = self.default_debtstackable,
            args = self.default_args,
            card_draw_hook = self.default_card_draw_hook or (lambda s, g, p: None)
        )

    def on_draw(self, fun: Callable[[Card[T], Game, Player], None]):
        self.default_card_draw_hook = fun




def card[*Ts](
    default_color: CardColor,
    default_penalty_points: int,
    default_card_type: str,
    default_debtstackable: bool = False,
    default_number_value : int = 0,
    default_rules: str | None = None,
    args: ArgBuilder[Game, *Ts] = ArgBuilder[Game]()
):
    def decorator(fun: Callable[[Game, *Ts], None]) -> CardFactory[Game]:
        return CardFactory[Game](
            default_color = default_color,
            default_rules = default_rules or fun.__doc__ or "This card has no rules text! You should probably fix that!",
            default_penalty = default_penalty_points,
            default_type = default_card_type,
            default_numerical_value = default_number_value,
            default_debtstackable = default_debtstackable,
            default_args = args.with_callback(fun)
        )
    return decorator


# todo split
def reverse_skip_draw(reverse: bool, skips: int, draws: int) -> CardFactory[Game]:
    assert draws >= 0 and skips >= 0
    assert reverse or draws > 0 or skips > 0

    card_types: list[str] = []
    card_name: list[str] = []
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
        default_color = CardColor.RED,
        default_penalty_points = 30,
        default_card_type = "_".join(card_types),
        default_debtstackable = draws > 0
    )
    def factory(game: Game):
        if reverse:
            game.table.reverse_direction()

        if skips > 0:
            game.table.skip(skips)

        if draws > 0:
            game.card_debt += draws

    return factory
