from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from game import Game
else:
    Game = Any

__all__ = ['Game'] # this file exists just to put all the circular import hacks in one place