# TODO: this being named abc doesn't make sense anymore -cap

from typing import TYPE_CHECKING, Any
from uuid import UUID, uuid4
import os.path
import util.image_util

from dataclasses import dataclass, field


from card.color import CardColor
from PIL import Image
from .argfunc import ArgFunc

# TODO: this solves circular dependency, but it's probably better to just refactor so that the type doesn't exist in the first place -cap
if TYPE_CHECKING:
    from game import Game
else:
    Game = Any
    CardArg = Any
    CardView = Any
    Player = Any


@dataclass
class Card[T]:
    color: CardColor # the card's color
    rules: str # the rules text of the card
    penalty_points: int # the card's penalty point value
    number_value: int # the card's value when treated as a number (e.g metadraw)
    card_type: str # the type of the card, used for matching rules
    can_play_on_debt: bool # whether or not this card is stackable when you have card debt
    raw_name: str # the pre-formatted display name

    # hooks
    # TODO: actually hook the hook
    type CardFunc = ArgFunc[T, T]
    on_play: CardFunc
    on_draw: CardFunc
    
    # autogenerate UUID
    uuid: UUID = field(default_factory=uuid4)

    # Checks whether this card can be played on a given pile
    # Defaults to standard UNO rules (at least one matching color OR matching card type)
    # todo: hookify this
    def can_play(self, game: Game, pile_index: int):
        # TODO: these and the other methods which reference Game should be moved to Game imo -cap
        top_card = game.piles[pile_index][-1]
        if game.card_debt > 0 and not self.can_play_on_debt:
            return False
        return bool(top_card.color & self.color) or self.card_type == top_card.card_type

    def playable_piles(self, game: Game):
        '''Returns a list of piles that this card can be played on.'''

        return [i for i in range(len(game.piles)) if self.can_play(game, i)]

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

    @property
    def display_name(self) -> str:
        # todo: do this in a nicer way, please
        return self.raw_name.replace(
            "%C", self.color.display_name
        ).replace(
            "%A", self.color.article.title()
        )
