import uuid
from typing import TYPE_CHECKING, Any
from PIL import Image
import util.image_util
import discord

# yet another circular dependency
if TYPE_CHECKING:
    from card import Card
else:
    Card = Any

# A collection of cards in a Player's hand
class Hand:
    def __init__(self):
        self.cards : list[Card] = []

    def __len__(self) -> int:
        return len(self.cards)

    def add_card(self, c: Card):
        self.cards.append(c)

    def lookup_card(self, u: uuid.UUID) -> Card | None:
        for c in self.cards:
            if c.uuid == u:
                return c
        return None

    def remove_card(self, c: Card):
        self.cards.remove(c)

    def sorted(self) -> list[Card]:
        out : list[Card] = self.cards[:]
        return sorted(out, key=lambda x: x.sort_key())

    def display_all_cards(self) -> str:
        return "\n".join(i.display_name for i in self.sorted())

    def render_all_cards(self) -> list[Image.Image]:
        '''
        Gives a sorted list of renders of cards in hand.
        '''
        return [i.render() for i in self.sorted()]

    def render(self) -> Image.Image:
        '''
        Renders this hand into a single image.
        Currently, that image is a 1xN row of the cards in hand.
        '''
        return util.image_util.image_row(self.render_all_cards())

    def render_discord(self) -> discord.File:
        '''
        As render, but outputs a discord.File
        '''
        return util.image_util.as_discord_file(self.render(), "hand.png")

    def __iter__(self):
        return self.cards.__iter__()
