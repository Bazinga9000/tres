import abc

import discord
from card.color import CardColor

class Card(abc.ABC):
    def __init__(self,
        color: CardColor, # The card's color
        point_value: int, # How much the card is worth when unplayed at the end of the round
        number_value: int, # The card's value, if treated as a number in-game
        card_type: str # The type of the card (by default, cards are playable on cards of the same type)
    ):
        self.color = color
        self.point_value = point_value
        self.number_value = number_value
        self.card_type = card_type

        # The display name of the card. Used to textually represent a card.
        # This defualt value should be overridden if the card has a special naming scheme (e.g is in only one color)
        self.display_name = f"{self.color_name()} {self.card_type}"

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
    # todo: annotating game with its type of Game causes a circular import dependency. figure out how to fix this
    def can_play(self, game, pile_index: int):
        top_card = game.piles[pile_index][-1]
        return bool(top_card.color & self.color) or self.card_type == top_card.card_type
