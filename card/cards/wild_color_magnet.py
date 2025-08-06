from typing import override

from card import Card
from card.color import ALL_COLORS, CardColor
from . import Game
from views.argbuilder import ArgBuilder


class WildColorMagnet(Card):
    def __init__(self):
        super().__init__(ALL_COLORS, 50, 0, "wild_color_magnet", False)
        self.display_name = "Wild Color Magnet"

    @property
    @override
    def args(self):
        return ArgBuilder[Game]().add_color().with_callback(self.on_play)

    def on_play(self, game: Game, color: CardColor):
        self.color = color
        self.display_name = f'{self.color_name()} {self.display_name}'

        next = game.table.next_player
        while True:
            c = game.deck.draw_from_deck()
            next.hand.add_card(c)

            if c.color == self.color: # todo: should this be an exact match?
                break
