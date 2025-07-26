import card.args.abc as ca
import discord

# Requests a player
class PlayerArg(ca.CardArg):
    def __init__(self, card: ca.Card, label: str, allow_self: bool, min_choices: int=1, max_choices: int=1):
        super().__init__(card, label, min_choices=min_choices, max_choices=max_choices)
        self.allow_self = allow_self

    def populate(self, game: ca.Game, player: discord.Member | discord.User, selected_pile: int, str_args: list[str]):
        self.values = [game.find_player_id(int(i)) for i in str_args]

    def generate(self, game: ca.Game, player: discord.Member | discord.User, selected_pile: int) -> list[tuple[str,str]]:
        options : list[tuple[str, str]] = []
        for p in game.players:
            if self.allow_self or p != player:
                options.append((p.display_name, str(p.id)))

        return options
