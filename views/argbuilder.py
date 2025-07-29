from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Callable, overload, override
from uuid import UUID

from discord import SelectOption
from discord.ui import View

from card.color import CardColor
from util.event import Event
from .select.typed import TypedSelect

# TODO: more cyclic imports
if TYPE_CHECKING:
    from game import Game
    from card import Card
else:
    Game = Card = Any

type SelectFactory[T] = Callable[[Game], TypedSelect[T]]
type Self[*T] = ArgBuilder[*T]


class ArgBuilderBase(ABC):
    @abstractmethod
    def compile(self, game: Game, view: View) -> Callable[[], object]:
        '''Compiles the argument list into a set of select options on the view and produces a callback.'''


class ArgBuilder[*Ts](ArgBuilderBase):
    @overload
    def __init__(self: Self[()]) -> None:
        ...

    @overload
    def __init__[*H, T](self: Self[*H, T], data: tuple[Self[*H], SelectFactory[T]]) -> None:
        ...

    def __init__[*H, T](self, data: tuple[Self[*H], SelectFactory[T]] | None = None):
        self.data = data
        self.callback = Event[Game, tuple[*Ts]]()

    def add[T](self, select: SelectFactory[T]) -> Self[*Ts, T]:
        return ArgBuilder((self, select))

    def add_player(self, placeholder: str = 'Select a player.', *, skip_self: bool):
        def factory(game: Game):
            def converter(value: str):
                player = game.find_player_id(int(value))
                if player is None:
                    raise ValueError('Selected player not found in game.')
                return player
            select = TypedSelect(converter)
            select.placeholder = placeholder
            select.options = [
                SelectOption(label=player.display_name, value=str(player.id))
                for player in game.players
                if player != game.active_player or not skip_self
            ]
            return select

        return self.add(factory)


    def add_card(self, placeholder: str = 'Select a card.', *, requires_playable: bool):
        def factory(game: Game):
            def converter(value: str):
                card = game.active_player.hand.lookup_card(UUID(value))
                if not card:
                    raise ValueError("Selected card index out of range.")
                return card

            select = TypedSelect(converter)
            select.placeholder = placeholder
            # todo: you shouldn't be able to choose the same card you're playing
            select.options = [
                SelectOption(label=card.display_name, value=str(card.uuid))
                for card in game.active_player.hand
                if card.playable_piles(game) or not requires_playable
            ]
            return select
        return self.add(factory)

    def add_color(self, placeholder: str = 'Select a color.'):
        def factory(game: Game):
            def converter(value: str):
                return CardColor(int(value))
            select = TypedSelect(converter)
            select.placeholder = placeholder
            select.options = [
                SelectOption(label=(color.name or '???').capitalize(), value=str(color.value))
                for color in CardColor
            ]
            return select
        return self.add(factory)

    def add_pile(self, placeholder: str = 'Select a pile.', *, playable_by: Card | None = None):
        def factory(game: Game):
            def converter(value: str):
                pile = int(value)
                if not 0 <= pile < len(game.piles):
                    raise ValueError('Selected pile index out of range.')
                return pile
            select = TypedSelect(converter)
            select.placeholder = placeholder
            select.options = [
                SelectOption(label=f'Pile #{i + 1}', value=str(i))
                for i in range(len(game.piles))
                if not playable_by or playable_by.can_play(game, i)
            ]
            return select
        return self.add(factory)

    def add_number(self, placeholder: str='Select a number.', *, min: int, max: int):
        def factory(game: Game):
            def converter(value: str):
                n = int(value)
                if not min <= n <= max:
                    raise ValueError("Out of bounds number given")
                return n

            select = TypedSelect(converter)
            select.placeholder = placeholder
            select.options = [
                SelectOption(label=str(n), value=str(n))
                for n in range(min, max+1)
            ]
            return select
        return self.add(factory)

    def with_callback(self, func: Callable[[Game, *Ts], None]):
        self.callback.subscribe(lambda game, args: func(game, *args))
        return self

    @override
    def compile(self, game: Game, view: View) -> Callable[[], tuple[*Ts]]:
        '''Compiles the argument list into a set of select options on the view and produces an interaction callback.'''

        if self.data:
            head, factory = self.data
            get_head_values = head.compile(game, view)

            # SIDE EFFECTS: add select to view
            select = factory(game)
            view.add_item(select)

            def get_values() -> tuple[*Ts]:
                values: tuple[*Ts] # necessary evil because pyright won't admit (*H, T) = *Ts
                values = (*get_head_values(), select.get_value()) # type: ignore
                self.callback(game, values)
                return values
            return get_values
        return lambda: () # type: ignore
