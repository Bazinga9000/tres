from typing import override
from card import Card
from card.color import CardColor
from . import Game
from game_components import Player
from views.argbuilder import ArgBuilder


class HandSwap(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, f"hand_swap", False)
    
    @property
    @override
    def args(self):
        return ArgBuilder[Game]().add_player(skip_self=True).with_callback(self.on_play)
    
    def on_play(self, game: Game, player: Player):
        player.hand, game.active_player.hand = game.active_player.hand, player.hand
