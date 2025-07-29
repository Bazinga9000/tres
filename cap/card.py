from dataclasses import dataclass, field
from enum import Flag, auto
from typing import Callable
from uuid import UUID, uuid4

from game_components.player import Player
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

@dataclass(frozen=True)
class Card[T]:
    color: CardColor
    rules: str
    penalty_points: int
    number_value: int
    card_type: str
    can_play_on_debt: bool
    
    args: ArgBuilderBase[T]
    uuid: UUID = field(default_factory=uuid4)

def card[*Ts](args: ArgBuilder[Game, *Ts] = ArgBuilder[Game]()):
    def decorator(func: Callable[[Game, *Ts], None]):
        def wrapper(color: CardColor, number_value: int):
            return Card(
                color=color,
                rules=func.__doc__ or "",
                penalty_points=number_value,
                number_value=number_value,
                card_type=func.__name__,
                can_play_on_debt=False,
                args=args.with_callback(func)
            )
        return wrapper
    return decorator

@card(
    ArgBuilder[Game]()
        .add_player('Select a player to swap hands with.', skip_self=True)
)
def hand_swap(game: Game, player: Player):
    '''Swap hands with a player of your choice.'''
    
    player.hand, game.active_player.hand = game.active_player.hand, player.hand
