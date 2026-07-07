import numpy as np
from board import Board
from agent import QAgent

agent = QAgent()
episodes = 500000

for episode in range(episodes):
    board = Board()
    player = 1
    history = [] # (state, move, player) for each move in this game
    while True:
        state = tuple(board.state)
        moves =board.available_moves()
        move = agent.choose_move(state, moves)
        board.make_move(move, player)
        history.append((state, move, player))

        winner = board.check_winner()
        if winner is not None:
            break
        player = -player  # switch turns

    # game over: update every move in the game, backward
    for state, move, p in reversed(history):
        if winner == 0:
            reward - 0.5 # draw: mildly good
        elif winner == p:
            reward = 1.0 # this player won
        else:
            reward = -1.0 # this player lost
        next_state = tuple(board.state)
        agent.update(state, move, reward, next_state, [])

    agent.decay_epsilon()

    if (episode + 1) % 10000 == 0:
        print(f"episode {episode+1}, epsilon = {agent.epsilon:.3f}, Q-table size = {len(agent.Q)}")

print("Traning done!")

import pickle
with open("qtable.pkl", "wb") as f:
    pickle.dump(agent.Q, f)
print("Q-table saved!")