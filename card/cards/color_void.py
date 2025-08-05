from typing import override
from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder

class ColorVoid(Card):
    def __init__(self, color: CardColor):
        super().__init__(color, 30, 0, "color_void", False)

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        me = game.piles[game.active_pile].pop()
        for card in [c for c in game.active_player.hand if bool(c.color & self.color)]:
            game.active_player.hand.remove_card(card)
            game.piles[game.active_pile].append(card)
        game.piles[game.active_pile].append(me)
