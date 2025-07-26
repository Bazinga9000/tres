from enum import Enum, auto


# What can cards ask for?
class CardArgType(Enum):
    Player = auto() # Any player, including yourself
    AnotherPlayer = auto() # A player, not including yourself
    PlayableCard = auto() # A card in your hand that can be played on the pile you're playing this card on, excluding this card
    AnyCard = auto() # A card in your hand, regardless of whether its playable
    Color = auto() # A single color, does NOT include colorless or combo/colors

    Arbitrary = auto() # An arbitrary set of choices, as determined by the card's get_custom_arg_choices function


# Something a card is able to ask for before it is played
# Each of these corresponds to a select option in the view
class CardArg():
    def __init__(self, type: CardArgType, label: str, min: int = 1, max:int = 1):
        assert max >= min
        assert min > 0
        self.arg_type = type # What is the card asking for?
        self.min = min # What's the minimum number of options?
        self.max = max # Whats the maximum number of options?
        self.label = label # What should be shown to the user?
