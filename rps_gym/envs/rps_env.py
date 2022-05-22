from enum import IntEnum, Enum
from random import randint
from telnetlib import GA

from gym import Env, spaces



class RPS(IntEnum):
    ROCK = 0
    SCISSORS = 1
    PAPER = 2

class GameState(float, Enum):
    WIN = 1.0
    TIE = 0.1
    LOSS = 0.0

SESSION_TO_GAMESTATE = {
    (RPS.ROCK, RPS.ROCK): GameState.TIE,
    (RPS.ROCK, RPS.SCISSORS): GameState.LOSS,
    (RPS.ROCK, RPS.PAPER): GameState.WIN, 
    (RPS.SCISSORS, RPS.ROCK): GameState.WIN,
    (RPS.SCISSORS, RPS.SCISSORS): GameState.TIE,
    (RPS.SCISSORS, RPS.PAPER): GameState.LOSS,
    (RPS.PAPER, RPS.ROCK): GameState.LOSS,
    (RPS.PAPER, RPS.SCISSORS): GameState.WIN,
    (RPS.PAPER, RPS.PAPER): GameState.TIE,
}


class RPSEnv(Env):
    def __init__(self, best_of=3) -> None:
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Discrete(3)
        self.ai_action = None

        self.best_of = best_of
        self.ai_wins = 0
        self.agent_wins = 0



    def reset(self):
        self.ai_wins = 0
        self.agent_wins = 0
        self.ai_action = RPS(randint(0, 2))
        return self.ai_action

    def step(self, action):
        done = False
        reward = SESSION_TO_GAMESTATE[(self.ai_action, RPS(action))]
        info = {}

        if reward == GameState.WIN:
            self.agent_wins += 1
        if reward == GameState.LOSS:
            self.ai_wins += 1

        self.ai_action = RPS(randint(0, 2))
        observation = self.ai_action

        if self.ai_wins == self.best_of or self.agent_wins == self.best_of:
            done = True
            observation = None
            info = {"agent_won": self.agent_wins == self.best_of}
            
        return observation, reward, done, info

    def render(self):
        pass

    def close(self):
        pass