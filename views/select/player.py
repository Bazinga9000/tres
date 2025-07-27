from typing import TYPE_CHECKING, Any, override
from game_components import Player
from .base import BaseSelect

if TYPE_CHECKING:
    from game import Game
else:
    Game = Any

class PlayerSelect(BaseSelect[Player]):
    def __init__(self, game: Game, placeholder: str, *, skip_self: bool):
        super().__init__(game, placeholder)
        active_player = self.game.players[self.game.whose_turn]
        for player in self.game.players:
            if player != active_player or not skip_self:
                self.select.add_option(label=player.display_name, value=str(player.id))

    @override
    def get_value(self) -> Player:
        player = self.game.find_player_id(int(self.get_raw_value()))
        if player is None:
            raise ValueError('Selected player not found in game.')
        return player
