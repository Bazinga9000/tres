import card.args.abc as ca
import discord

# Requests cards in the player's hand (other than the card that is asking for the args)
class CardInHandArg(ca.CardArg):
    def __init__(self, card: ca.Card, label: str, restrict_to_playable: bool, min_choices: int=1, max_choices: int=1):
        super().__init__(card, label, min_choices=min_choices, max_choices=max_choices)
        self.restrict_to_playable = restrict_to_playable

    def populate(self, game: ca.Game, player: discord.Member | discord.User, selected_pile: int, str_args: list[str]):
        self.values = [game.hands[player][int(i)] for i in str_args]


    def generate(self, game: ca.Game, player: discord.Member | discord.User, selected_pile: int) -> list[tuple[str,str]]:
        options : list[tuple[str, str]] = []
        for (k,c) in enumerate(game.hands[player]):
            if c != self.card: # A card can never select itself
                if (not self.restrict_to_playable) or c.can_play(game, selected_pile):
                   options.append((c.display_name, str(k)))

        return options
