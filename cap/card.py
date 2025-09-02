from discord.ui.view import View
from .argfunc import ArgFunc
from game import Game


from discord import SelectOption
from discord.ui import View
from game import Game
from views.select.base import BaseSelect


def compile_selects(func: ArgFunc[Game, Game], view: View, game: Game):
    def build_select(options: list[str]):
        select = BaseSelect()
        select.options = [SelectOption(label=opt, value=opt) for opt in options]
        view.add_item(select)
        return select.get_raw_value
    return func.compile(build_select, game)


def card[*Ts](
    default_penalty_points: int = 0,
    default_card_type: str | None = None,
    default_raw_name: str | None = None,
    default_debtstackable: bool = False,
    default_number_value : int = 0,
    default_rules: str | None = None
):
    def decorator(fun: ArgFunc[Game, Game].Inner) -> None:
        on_play: ArgFunc[Game, Game] = ArgFunc(fun, lambda g: [], lambda g: lambda s: g)
        
        # to create select menu
        view: View = ... # type: ignore
        game: Game = ... # type: ignore
        compile_selects(on_play, view, game)
    
    return decorator
