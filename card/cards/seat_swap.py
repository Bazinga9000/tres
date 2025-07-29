from typing import override
from card import Card
from card.color import CardColor
from . import Game
from game_components import Player
from views.argbuilder import ArgBuilder


class SeatSwap(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, "seat_swap", False)

    @property
    @override
    def args(self):
        return ArgBuilder[Game]().add_player(skip_self=True).with_callback(self.on_play)

    def on_play(self, game: Game, player: Player):
        my_seat = game.whose_turn
        their_seat = game.players.index(player)
        game.players[my_seat], game.players[their_seat] = game.players[their_seat], game.players[my_seat]
        game.whose_turn = their_seat
