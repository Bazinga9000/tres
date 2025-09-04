from core.cards import ArgFunc, Argument, Card, CardColor
from game import Game

from typeutils import F


def card(
    penalty: int = 0,
    card_type: str | None = None,
    raw_name: str | None = None,
    can_play_on_debt: bool = False,
    number_value : int = 0,
    rules: str | None = None
):
    # we can't directly use @decorates here because fun isn't necessarily a function TODO: you know what would be really funny...
    def decorator(fun: ArgFunc[Game, Game].Inner) -> F[[CardColor], Card[Game]]:
        get_game: F[[Game], Argument[Game]] = lambda g: Argument(placeholder='', options=(), default=g)
        on_play = ArgFunc(fun, get_game)
        on_draw = ArgFunc(lambda g: None, get_game)
        
        # TODO: we probably have to turn this into a class again...
        # idea to reduce repetition: make the CardFactory store the below function instead of all the values
        def wrapper(color: CardColor) -> Card[Game]:
            return Card(
                color=color,
                rules=rules or fun.__doc__ or "This card has no rules text! You should probably fix that!",
                penalty_points=penalty,
                number_value=number_value,
                card_type=card_type or fun.__name__,
                raw_name=raw_name or '%C ' + (card_type or fun.__name__).replace('_',' ').title(), # TODO: default raw_name should probably be handled by the card -cap
                can_play_on_debt=can_play_on_debt,
                on_play=on_play,
                on_draw=on_draw
            )
        # we can't directly use wraps here because fun isn't necessarily a function
        wrapper.__name__ = fun.__name__
        wrapper.__doc__ = fun.__doc__
        wrapper.__module__ = fun.__module__
        wrapper.__qualname__ = fun.__qualname__
        wrapper.__annotations__ = fun.__annotations__
        
        return wrapper
    return decorator
