import abc
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, Awaitable
import uuid

from discord import Interaction

from card.color import CardColor


# TODO: this solves circular dependency, but it's probably better to just refactor so that the type doesn't exist in the first place -cap
if TYPE_CHECKING:
    from game import Game
    from views.cardview import CardView # i made it even worse -cap
    from game_components import Player # absolute cinema - baz
else:
    Game = Any
    CardArg = Any
    CardView = Any
    Player = Any

class Card(abc.ABC):
    def __init__(self,
        color: CardColor, # The card's color
        penalty_points: int, # How much the card is worth when unplayed at the end of the round
        number_value: int, # The card's value, if treated as a number in-game
        card_type: str, # The type of the card (by default, cards are playable on cards of the same type)
        can_play_on_debt: bool # Can you play this card while you have card debt?
    ):
        self.color = color
        self.penalty_points = penalty_points
        self.number_value = number_value
        self.card_type = card_type
        self.can_play_on_debt = can_play_on_debt

        # The uuid of a card.
        # Todo. Have it change if the card is cloned to ensure uniqueness
        self.uuid = uuid.uuid4()

        # The display name of the card. Used to textually represent a card.
        # This defualt value should be overridden if the card has a special naming scheme (e.g is in only one color)
        self.display_name = f"{self.color_name()} {self.card_type}".replace("_"," ").title()

    # Gets the color name of this card, used to
    def color_name(self):

        color_names = {
            CardColor.RED: "Red",
            CardColor.ORANGE: "Orange",
            CardColor.YELLOW: "Yellow",
            CardColor.GREEN: "Green",
            CardColor.BLUE: "Blue",
            CardColor.PURPLE: "Purple"
        }

        return "/".join(v for (k,v) in color_names.items() if k in self.color)

    # Checks whether this card can be played on a given pile
    # Defaults to standard UNO rules (at least one matching color OR matching card type)
    def can_play(self, game: Game, pile_index: int):
        top_card = game.piles[pile_index][-1]
        if game.card_debt > 0 and not self.can_play_on_debt:
            return False
        return bool(top_card.color & self.color) or self.card_type == top_card.card_type

    def playable_piles(self, game: Game):
        '''Returns a list of piles that this card can be played on.'''

        return [i for i in range(len(game.piles)) if self.can_play(game, i)]

    # Called *after* the card is put into the hand
    def on_draw(self, game: Game, player: Player):
        pass

    @abc.abstractmethod
    def on_select(self, view: CardView) -> Callable[[Interaction], Awaitable[None]]:
        '''Runs when the card is selected in the card view.'''
