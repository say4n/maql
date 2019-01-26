"""
Gridworld Soccer Game

paper - https://www2.cs.duke.edu/courses/spring07/cps296.3/littman94markov.pdf

:: game description ::

The game is played on a 4x5 grid as depicted in Figure 2. The two players, A and B, occupy distinct squares of the grid and can choose one of 5 actions on each turn: N, S, E, W, and stand. Once both players have selected their actions, the two moves are executed in random order.

The circle in the figures represents the “ball.” When the player with the ball steps into the appropriate goal (left for A, right for B), that player scores a point and the board is reset to the configuration shown in the left half of the figure. Possession of the ball goes to one or the other player at random.

When a player executes an action that would take it to the square occupied by the other player, possession of the ball goes to the stationary player and the move does not take place. A good defensive maneuver, then, is to stand where the other player wants to go. Goals are worth one point and the discount factor is set to 0.9, which makes scoring sooner somewhat better than scoring later.

  # # # # #
# # # # # # #
# # # # # # #
  # # # # #

"""

import numpy as np
import random


BOARD_HEIGHT = 4
BOARD_LENGTH = 5

nodes = list(range(20))


class Soccer:
    BLANK = 0
    PLAYER_A = 1
    PLAYER_B = 2
    BALL = 3

    BOARD_H = 4
    BOARD_W = 5

    ACTION_UP = 100
    ACTION_DOWN = 101
    ACTION_LEFT = 102
    ACTION_RIGHT = 103
    ACTION_STAY = 104

    ACTION_PROBABILITY = 0.5


    def __init__(self):
        self.game = np.array([[Soccer.BLANK for _ in range(Soccer.BOARD_W)] for _ in range(Soccer.BOARD_H)])

        self.action_space = [Soccer.ACTION_UP, Soccer.ACTION_DOWN,
                             Soccer.ACTION_LEFT, Soccer.ACTION_RIGHT,
                             Soccer.ACTION_STAY]

        self.position_a = None
        self.position_b = None
        self.ball_possessor = None

        self.reset()


    def reset(self):
        self.ball_possessor = random.choice([Soccer.PLAYER_A, Soccer.PLAYER_B])

        self.position_a = random.choice(range(Soccer.BOARD_H * Soccer.BOARD_W))
        self.position_b = random.choice(range(Soccer.BOARD_H * Soccer.BOARD_W))

        if self.position_b == self.position_a:
            self.position_b = (self.position_b + 1) % \
                                (Soccer.BOARD_H * Soccer.BOARD_W)

        self.game[self.index2pos(self.position_a)] = Soccer.PLAYER_A
        self.game[self.index2pos(self.position_b)] = Soccer.PLAYER_B


    def action(self, action_a, action_b):
        if random.random() > self.ACTION_PROBABILITY:
            # action_a followed by action_b
            self.move(Soccer.PLAYER_A, action_a)
            self.move(Soccer.PLAYER_B, action_b)

            reward = 0
        else:
            # action_a followed by action_b
            self.move(Soccer.PLAYER_B, action_b)
            self.move(Soccer.PLAYER_A, action_a)

            reward = 0

        return reward


    def move(self, agent, action):
        if agent == Soccer.PLAYER_A:
            position = self.position_a
            player = "Player A"
        elif agent == Soccer.PLAYER_B:
            position = self.position_b
            player = "Player B"
        else:
            raise Exception(f"Invalid player ID {agent}")


        if action == ACTION_UP
            self.position_a = self.is_valid_move(position, ACTION_UP):
            pass
        elif action == ACTION_DOWN and self.is_valid_move(position,
                                                          ACTION_DOWN):
            pass
        elif action == ACTION_LEFT and self.is_valid_move(position,
                                                          ACTION_LEFT):
            pass
        elif action == ACTION_RIGHT and self.is_valid_move(position,
                                                           ACTION_RIGHT):
            pass
        elif action == ACTION_STAY and self.is_valid_move(position,
                                                          ACTION_STAY):
            pass


    def index2pos(self, index):
        row = index // Soccer.BOARD_W
        col = index - row * Soccer.BOARD_W

        return row, col


    def pos2index(self, row, col):
        return row * Soccer.BOARD_W + col


    def is_valid_move(self, current_pos, move):
        pass

    def __repr__(self):
        ret = ""
        for row in self.game:
            for cell in row:
                if cell == Soccer.BLANK:
                    ret += " * "
                elif cell == Soccer.PLAYER_A:
                    if self.ball_possessor == Soccer.PLAYER_A:
                        ret += " A."
                    else:
                        ret += " A "
                elif cell == Soccer.PLAYER_B:
                    if self.ball_possessor == Soccer.PLAYER_B:
                        ret += " B."
                    else:
                        ret += " B "
            ret += "\n"

        return ret

if __name__ == '__main__':
    game =  Soccer()
    print(game)
