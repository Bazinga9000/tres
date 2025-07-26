import abc
from typing import Any
from card.abc import Card
import discord
from typing import TYPE_CHECKING

# todo: fix yet another circular type dependency --baz
if TYPE_CHECKING:
    from game import Game
else:
    Game = Any

class CardArg(abc.ABC):
    def __init__(self, card: Card, label: str, min_choices: int = 1, max_choices: int = 1):
        assert max_choices >= min_choices >= 1
        self.card = card
        self.min_choices = min_choices
        self.max_choices = max_choices

        self.label = label
        self.values : list[Any] | None = None

    # Populate the argument's values given the strings passed from the selector
    @abc.abstractmethod
    def populate(self, game: Game, player: discord.Member | discord.User, selected_pile: int, str_args: list[str]):
        pass

    # Generate the options for the selector
    @abc.abstractmethod
    def generate(self, game: Game, player: discord.Member | discord.User, selected_pile: int) -> list[tuple[str, str]]:
        pass

    # Am I fully populated with choices?
    def is_populated(self):
        if self.values is None: return False
        return self.max_choices >= len(self.values) and len(self.values) >= self.min_choices
