from dataclasses import dataclass
from typing import Callable

from game import Game
from game_components import Player
from views.argbuilder import ArgBuilder, ArgBuilderBase
from .abc import Card
from .color import CardColor

@dataclass
class CardFactory[T]:
    default_rules: str
    default_penalty: int
    default_numerical_value: int
    default_type: str
    default_debtstackable: bool
    default_raw_name: str
    default_args: ArgBuilderBase[T]
    default_card_draw_hook: Callable[[Card[T], Game, Player], None] | None = None

    def __call__(self, color: CardColor) -> Card[T]:
        return Card(
            color = color,
            rules = self.default_rules,
            penalty_points = self.default_penalty,
            number_value = self.default_numerical_value,
            card_type = self.default_type,
            raw_name = self.default_raw_name,
            can_play_on_debt = self.default_debtstackable,
            args = self.default_args,
            card_draw_hook = self.default_card_draw_hook or (lambda s, g, p: None)
        )

    def on_draw(self, fun: Callable[[Card[T], Game, Player], None]):
        self.default_card_draw_hook = fun


def card[*Ts](
    default_penalty_points: int,
    default_card_type: str | None = None,
    default_raw_name: str | None = None,
    default_debtstackable: bool = False,
    default_number_value : int = 0,
    default_rules: str | None = None,
    args: ArgBuilder[Game, *Ts] = ArgBuilder[Game]()
):
    def decorator(fun: Callable[[Game, *Ts], None]) -> CardFactory[Game]:
        t = default_card_type or fun.__name__
        return CardFactory[Game](
            default_rules = default_rules or fun.__doc__ or "This card has no rules text! You should probably fix that!",
            default_penalty = default_penalty_points,
            default_type = t,
            default_raw_name = default_raw_name or f"%C {t.replace("_"," ").title()}",
            default_numerical_value = default_number_value,
            default_debtstackable = default_debtstackable,
            default_args = args.with_callback(fun)
        )
    return decorator

def constant_color(color: CardColor):
    def decorator(fun: Callable[[CardColor], Card[Game]]) -> Callable[[], Card[Game]]:
        return lambda: fun(color)
    return decorator
