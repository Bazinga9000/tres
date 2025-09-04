import os.path
from uuid import UUID, uuid4
from dataclasses import dataclass, field

from PIL import Image

from .argfunc import ArgFunc
from .color import CardColor
import util.image_util


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
    # TODO: actually hook the draw hook
    type CardFunc = ArgFunc[T, T]
    on_play: CardFunc
    on_draw: CardFunc
    
    # autogenerate UUID
    uuid: UUID = field(default_factory=uuid4)
    
    def render(self) -> Image.Image:
        assets_location = "assets"
        
        backs_location = f"{assets_location}/card_backs"
        card_back = f"{backs_location}/{self.color.name.lower()}.png"
        if not os.path.isfile(card_back):
            card_back = f"{backs_location}/wild.png"
        
        symbols_location = f"{assets_location}/symbols"
        symbol = f"{symbols_location}/{self.card_type}.png"
        if not os.path.isfile(symbol):
            symbol = f"{symbols_location}/placeholder.png"
        
        return util.image_util.compose_files([card_back, symbol])
    
    def sort_key(self) -> list[int]:
        key = list[int]()
        
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
                # TODO: more intelligent sorting of non-rainbow multicolored cards
                # this will, at least, put rainbow (all colors) last
                key.append(c.value + 7)
        
        # within each color, number cards are always first
        try:
            key.extend([0, int(self.card_type)])
        except:
            # card type isn't a bare integer
            key.append(1)
            # TODO: change this later, i guess?
            # sort by penalty points, highest last
            key.append(self.penalty_points)
            # if penalty points are the same, give up and just use the hash
            key.append(hash(self.card_type))
        
        # always break ties by the uuid
        key.append(int(self.uuid))
        
        return key
    
    @property
    def display_name(self) -> str:
        # TODO: do this in a nicer way, please
        return self.raw_name.replace(
            "%C", self.color.name
        ).replace(
            "%A", self.color.article.title()
        )
