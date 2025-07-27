from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from discord.ui.select import Select
from discord.ui.view import View

if TYPE_CHECKING:
    from game import Game
else:
    Game = Any



class BaseSelect[T](ABC):
    def __init__(self, game: Game):
        self.game = game
        self.select = self.initialize_select()
    
    @abstractmethod
    def initialize_select(self) -> Select[View]:
        ...
    
    @abstractmethod
    def get_value(self) -> T:
        ...
