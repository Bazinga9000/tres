import util.number_names

from .factory import CardFactory, card
from .color import CardColor
from game import Game

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
