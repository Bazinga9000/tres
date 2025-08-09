from typing import override
from card import Card
from card.color import CardColor
from . import Game
from views.argbuilder import ArgBuilder
import util.number_names

class PotOfGreed(Card):
    def __init__(self, color: CardColor, *, draw: int=2):
        assert draw >= 0
        self.d = draw

        card_types: list[str] = ['pot_of_greed']
        card_name: list[str] = ["Pot of Greed"]

        if self.d != 2:
            card_types.append(f"{self.d}")
            card_name.insert(0, util.number_names.tuple_name(self.d))

        super().__init__(color, 30, 0, "_".join(card_types), False)
        self.display_name = f"{self.color_name()} {' '.join(card_name)}"

    @property
    @override
    def args(self):
        return ArgBuilder().with_callback(self.on_play)

    def on_play(self, game: Game):
        for _ in range(self.d):
            game.active_player.hand.add_card(game.deck.draw_from_deck())
