from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from discord.ui import Select, View

if TYPE_CHECKING:
    from game import Game
else:
    Game = Any


class BaseSelect[T](ABC):
    def __init__(self, game: Game, placeholder: str):
        self.game = game
        self.select = Select[View](placeholder=placeholder)
    
    @abstractmethod
    def get_value(self) -> T:
        ...
    
    def get_raw_value(self) -> str:
        if not self.select.values:
            raise ValueError('No selection.')
        return str(self.select.values[0])
    
    def get_raw_values(self) -> list[str]:
        return [str(value) for value in self.select.values]
