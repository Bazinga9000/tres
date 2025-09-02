from .card import card
from .cardargs import *
from game import Game
from game_components import Player


@card()
def skip_turn(game: Game):
    ...

@card(default_number_value=9999999)
@choose_player
def eject_player(game: Game, player: Player):
    player.eject()

@card(default_rules='you have to play this card')
@choose_player
@choose_color
def change_player_to_color(game: Game, player: Player, color: CardColor):
    print(f'{player.display_name} is now {color.name}')
