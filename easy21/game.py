import random
from enum import Enum
from dataclasses import dataclass


class Colour(Enum):
    RED = 1
    BLACK = 2


COLOURS = [Colour.RED, Colour.BLACK]
COLOURS_DISTRIBUTION_WEIGHTS = [1, 2]


class Action(Enum):
    HIT = 1
    STICK = 2


class Result(Enum):
    AWAITING = 0
    WON = 1
    LOST = 2
    DRAW = 3


@dataclass
class Card:
    value: int
    colour: Colour

    def __init__(self):
        self.value = random.randint(1, 10)
        self.colour = random.choices(COLOURS, weights=COLOURS_DISTRIBUTION_WEIGHTS, k=1)[0]


@dataclass
class State:
    player_score: int
    is_game_over: bool
    result: Result

    def __init__(self, player_score: int, is_game_over: bool, result: Result):
        self.player_score = player_score
        self.is_game_over = is_game_over
        self.result = result


@dataclass
class Game:
    is_game_over: bool
    game_result: Result
    is_players_turn: bool
    player_score: int
    dealer_score: int

    def __init__(self):
        self.is_game_over = False
        self.game_result = Result.AWAITING
        self.is_players_turn = True
        self.player_score = Card().value
        self.dealer_score = Card().value

    @property
    def state(self):
        return State(self.player_score, self.is_game_over, self.game_result)

    def step(self, action: Action):
        if self.is_game_over:
            raise Exception("Game is already over")

        if self.is_players_turn:
            if action == Action.HIT:
                drawn = Card()
                print("player drawn " + str(drawn))
                self.player_score += drawn.value if drawn.colour is Colour.BLACK else -1 * drawn.value
                if 1 <= self.player_score <= 21:
                    pass
                else:
                    self.is_game_over = True
                    self.game_result = Result.LOST

                return self.state
            else:
                self.is_players_turn = False
        else:
            if self.dealer_score >= 17:
                self.is_game_over = True
                score = self.player_score - self.dealer_score
                self.game_result = Result.WON if score > 0 else Result.DRAW if score == 0 else Result.LOST
            else:
                drawn = Card()
                print("dealer drawn " + str(drawn))
                self.dealer_score += drawn.value if drawn.colour is Colour.BLACK else -1 * drawn.value
                if 1 <= self.dealer_score <= 21:
                    pass
                else:
                    self.is_game_over = True
                    self.game_result = Result.WON

                return self.state
