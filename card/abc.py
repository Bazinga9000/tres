import abc
from typing import TYPE_CHECKING, Any
import uuid
import os.path
import util.image_util


from card.color import CardColor
from views.argbuilder import ArgBuilder, ArgBuilderBase
from PIL import Image


# TODO: this solves circular dependency, but it's probably better to just refactor so that the type doesn't exist in the first place -cap
if TYPE_CHECKING:
    from game import Game
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

    @property
    def args(self) -> ArgBuilderBase[Game]:
        '''Returns the arguments for this card.'''

        return ArgBuilder()

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

    def render(self) -> Image.Image:
        assets_location = "assets"
        backs_location = f"{assets_location}/card_backs"

        match self.color:
            case CardColor.RED:
                card_back = f"{backs_location}/red.png"
            case CardColor.ORANGE:
                card_back = f"{backs_location}/orange.png"
            case CardColor.YELLOW:
                card_back = f"{backs_location}/yellow.png"
            case CardColor.GREEN:
                card_back = f"{backs_location}/green.png"
            case CardColor.BLUE:
                card_back = f"{backs_location}/blue.png"
            case CardColor.PURPLE:
                card_back = f"{backs_location}/purple.png"
            case _:
                card_back = f"{backs_location}/wild.png"

        symbols_location = f"{assets_location}/symbols"
        symbol = f"{symbols_location}/{self.card_type}.png"
        if not os.path.isfile(symbol):
            symbol = f"{symbols_location}/placeholder.png"

        return util.image_util.compose_files([card_back, symbol])

    def sort_key(self) -> list[int]:
        key : list[int] = []

        # first, sort by color
        match self.color:
            # Monocolored cards always go first
            case CardColor.RED:
                key.append(1)
            case CardColor.ORANGE:
                key.append(2)
            case CardColor.YELLOW:
                key.append(3)
            case CardColor.GREEN:
                key.append(4)
            case CardColor.BLUE:
                key.append(5)
            case CardColor.PURPLE:
                key.append(6)
            case c:
                # todo: more intelligent sorting of non-rainbow multicolored cards
                # this will, at least, put rainbow (all colors) last
                key.append(c.value + 7)

        # within each color, number cards are always first
        try:
            key.extend([0, int(self.card_type)])
        except:
            # card type isn't a bare integer
            key.append(1)
            # todo: change this later, i guess?
            # sort by penalty points, highest last
            key.append(self.penalty_points)
            # if penalty points are the same, give up and just use the hash
            key.append(hash(self.card_type))

        # always break ties by the uuid
        key.append(int(self.uuid))

        return key
