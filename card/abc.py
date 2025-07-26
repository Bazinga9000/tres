import abc

import discord
from card.color import CardColor

class Card(abc.ABC):
    def __init__(self,
        color: CardColor, # The card's color
        point_value: int, # How much the card is worth when unplayed at the end of the round
        number_value: int, # The card's value, if treated as a number in-game
        card_type: str, # The type of the card (by default, cards are playable on cards of the same type)
        can_play_on_debt: bool # Can you play this card while you have card debt?
    ):
        self.color = color
        self.point_value = point_value
        self.number_value = number_value
        self.card_type = card_type
        self.can_play_on_debt = can_play_on_debt

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
    # todo: annotating game with its type of Game causes a circular import dependency. figure out how to fix this
    def can_play(self, game, pile_index: int):
        top_card = game.piles[pile_index][-1]
        if game.card_debt > 0 and not self.can_play_on_debt:
            return False
        return bool(top_card.color & self.color) or self.card_type == top_card.card_type


    # Called *after* the card is put onto the top of its corresponding pile.
    def on_play(self, game, pile_index : int, card_args):
        pass

    # Called *after* the card is put into the hand
    def on_draw(self, game, player):
        pass

    # Return a dictionary mapping internal names to CardArgs.
    # on_play (above) will be passed a dictionary mapping these names to the list of given arguments
    # See wild_card for an example
    def get_args(self):
        return {}

    # If your card uses the Arbitrary card arg type, this function will be called to determine the set of possible options.
    # this should return a list of tuples (string to display in the selector, string to be passed to on_play)
    def get_custom_arg_choices(self, arg_id: str):
        return []
