from uuid import UUID
from game import Game
from pregame import PreGame


games: dict[UUID, PreGame | Game | None] = {}
def init():
    global games
    games = {}
