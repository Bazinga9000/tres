import uuid

import discord
from PIL import Image

import util.image_util
from .card import Card


class Hand[T]:
    '''A collection of cards in a player's hand.'''
    
    type Card = Card[T]
    
    def __init__(self):
        self.cards : list[Card[T]] = []

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
        out = self.cards[:]
        return sorted(out, key=lambda x: x.sort_key())

    def display_all_cards(self) -> str:
        return "\n".join(i.display_name for i in self.sorted())

    def penalty_value(self) -> int:
        '''
        Return the total amount of penalty points incurred by this hand.
        '''
        return sum(i.penalty_points for i in self)

    def is_public(self) -> bool:
        '''
        Based on the cards in this hand, should this hand be revealed?
        '''
        return any(i.card_type == "revelation" for i in self)

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
