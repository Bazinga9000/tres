from .argfunc import ArgFunc
from game import Game
from card.color import CardColor


@ArgFunc.create
def choose_player(game: Game):
    def converter(value: str):
        player = game.table.find_unejected_player_id(int(value))
        if player is None:
            raise ValueError('Selected player not found in game or was ejected.')
        return player
    return [str(player.id) for player in game.table.starting_with_you], converter

@ArgFunc.create
def choose_color(game: Game):
    def converter(value: str):
        return CardColor(int(value))
    return [str(color.value) for color in CardColor], converter
