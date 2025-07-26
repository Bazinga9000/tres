import card.args.abc as ca
import discord

from card.color import CardColor

# Requests single colors (that is, red or orange or ... or purple, no combos)
class ColorArg(ca.CardArg):
    def populate(self, game: ca.Game, player: discord.Member | discord.User, selected_pile: int, str_args: list[str]):
        self.values = [CardColor(int(i)) for i in str_args]

    def generate(self, game: ca.Game, player: discord.Member | discord.User, selected_pile: int) -> list[tuple[str,str]]:
        def serialize(c: CardColor) -> str:
            return str(c.value)

        color_options = [
            ("Red", CardColor.RED),
            ("Orange", CardColor.ORANGE),
            ("Yellow", CardColor.YELLOW),
            ("Green", CardColor.GREEN),
            ("Blue", CardColor.BLUE),
            ("Purple", CardColor.PURPLE)
        ]

        return [(i[0], serialize(i[1])) for i in color_options]
