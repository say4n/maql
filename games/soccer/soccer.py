"""
Gridworld Soccer Game

paper - https://www2.cs.duke.edu/courses/spring07/cps296.3/littman94markov.pdf

:: game description ::

The game is played on a 4x5 grid as depicted in Figure 2. The two players, A and B, occupy distinct squares of the grid and can choose one of 5 actions on each turn: N, S, E, W, and stand. Once both players have selected their actions, the two moves are executed in random order.

The circle in the figures represents the “ball.” When the player with the ball steps into the appropriate goal (left for A, right for B), that player scores a point and the board is reset to the configuration shown in the left half of the figure. Possession of the ball goes to one or the other player at random.

When a player executes an action that would take it to the square occupied by the other player, possession of the ball goes to the stationary player and the move does not take place. A good defensive maneuver, then, is to stand where the other player wants to go. Goals are worth one point and the discount factor is set to 0.9, which makes scoring sooner somewhat better than scoring later.
"""
