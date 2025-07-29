from typing import override

from card import Card
from card.color import CardColor
from game_components import Player
from . import Game
from views.argbuilder import ArgBuilder



class Kissaroo(Card):
    def __init__(self, c: CardColor):
        super().__init__(c, 50, 0, "kissaroo", False)
        if self.color_name()[0].lower() in ["a","e","i","o","u"]:
            article = "An"
        else:
            article = "A"

        self.display_name = f"{article} {self.color_name()} Kissaroo from Me to You"

    @property
    @override
    def args(self):
        return ArgBuilder[Game]().add_card(requires_playable=False).add_player(skip_self=True).with_callback(self.on_play)

    def on_play(self, game: Game, card: Card, target: Player):
        game.active_player.hand.remove_card(card)
        target.hand.add_card(card)
