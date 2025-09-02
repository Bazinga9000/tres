from game_components import Player, Hand
import random
from typing import Generator, Any, Iterator

class Table[T]:
    '''
    Represents the list of players and their seating order.

    Has methods for interacting with the turn and direction of play
    '''
    
    type Player = Player[T]
    
    def __init__(self, players: list[Player]):

        # Every player in the game.
        # Should never be modified.
        self.all_players = players

        # The list of players in the current round
        # This list determines the order of play.
        self.round_participants : list[Player[T]] = []

        # The index into turn_order of the player whose turn it is
        self.active_player_index = 0

        # Which way the turn order moves
        # Should always be 1 or -1
        self.direction_of_play = 1


    def populate_round(self):
        '''
        Empties all hands, un-eject all players, fills up self.round_participants with all players eligible to participate in the round, then shuffles the turn order.
        '''
        for p in self.all_players:
            p.ejected = False
            p.hand = Hand()

        self.round_participants = [p for p in self.all_players if not p.eliminated]
        self.direction_of_play = 1
        random.shuffle(self.round_participants)


    @property
    def active_player(self) -> Player:
        '''
        Returns the player whose turn it is.
        '''
        return self.round_participants[self.active_player_index]

    @property
    def next_player(self) -> Player:
        '''
        Returns the player who is next in the turn order.
        '''
        next_ind = self.next_unejected_index(self.active_player_index)
        return self.round_participants[next_ind]

    def next_unejected_index(self, cursor: int) -> int:
        '''
        Starting at the player at index cursor, return the index (in turn order) of the next player who is NOT ejected
        '''
        while True:
            cursor += self.direction_of_play
            cursor %= len(self.round_participants)
            if not self.round_participants[cursor].ejected:
                return cursor

    def tick(self):
        '''
        Advance the active player by one. This will skip over any ejected players.
        '''
        self.active_player_index = self.next_unejected_index(self.active_player_index)

    def skip(self, n: int):
        '''
        Advance the active player by n.
        '''
        for _ in range(n):
            self.tick()

    def reverse_direction(self):
        '''
        Reverse the direction of play.
        '''
        self.direction_of_play *= -1

    def swap_players(self, a: Player, b: Player):
        '''
        Swap the positions of two players in the turn order, adjusting the active player index if necessary.
        '''
        ap = self.active_player
        a_seat = self.round_participants.index(a)
        b_seat = self.round_participants.index(b)
        self.round_participants[a_seat], self.round_participants[b_seat] = self.round_participants[b_seat], self.round_participants[a_seat]
        if a == ap:
            self.active_player_index = b_seat
            return
        if b == ap:
            self.active_player_index = a_seat


    def turn_order_text(self) -> str:
        '''
        Returns a string representing the current turn order and direction of play.

        Will highlight the active player in **bold**
        Will ~~strike through~~ any ejected players.
        '''
        delimiter = " > " if self.direction_of_play == 1 else " < "

        ap = self.active_player
        return delimiter.join([
            p.formatted_display_name(ap) for p in self.turn_order
        ])

    def find_player_id(self, player_id: int) -> Player | None:
        '''
        Returns the player at this table corresponding to a given ID.
        '''
        for p in self.all_players:
            if p.id == player_id:
                return p

        return None

    def find_unejected_player_id(self, player_id: int) -> Player | None:
        '''
        Returns the player at this table corresponding to a given ID, if that player is playing in the current round and is not ejected.
        '''
        for p in self.round_participants:
            if p.id == player_id and not p.ejected:
                return p

        return None

    @property
    def turn_order(self) -> Iterator[Player]:
        '''
        Returns a list of players in the round in the current turn order.
        '''
        return self.round_participants.__iter__()


    def round_participants_iter(self, offset: int) -> Generator[Player, Any, None]:
        '''
        Returns a generator that yields all non-ejected round participants in turn order, starting offset players after (in turn order) the active player.
        '''
        non_ejected = len([i for i in self.round_participants if not i.ejected])
        start = (self.active_player_index + (offset * self.direction_of_play))%len(self.round_participants)
        def generator():
            cursor = start
            for _ in range(non_ejected):
                yield self.round_participants[cursor]
                cursor = self.next_unejected_index(cursor)

        return generator()


    @property
    def starting_with_you(self) -> Generator[Player, Any, None]:
        '''
        Iterates through all round participants, starting with the active player.
        '''
        return self.round_participants_iter(0)

    @property
    def starting_after_you(self) -> Generator[Player, Any, None]:
        '''
        Iterates through all round participants in turn order, starting with the player who is next after the active player.
        This will thus have the active player last in the iteration
        '''
        return self.round_participants_iter(1)
