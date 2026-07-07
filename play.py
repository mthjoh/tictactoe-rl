import os
import pickle
import numpy as np
from board import Board
from agent import QAgent

agent = QAgent(epsilon = 0)
if os.path.exists("qtable.pkl"):
    with open("qtable.pkl", "rb") as f:
        agent.Q = pickle.load(f)
    print("Loaded trained Q-table:", len(agent.Q), "entries")
else:
    print("No qtable.pkl found - playing against UNTRAINED agent (random moves)")

board = Board()
human, ai = -1, 1 # you are O, agent is X, agenet goes first

while True:
    #agent's turn
    state = tuple(board.state)
    move = agent.choose_move(state, board.available_moves())
    board.make_move(move, ai)
    print("Agent plays:")
    board.show()
    winner = board.check_winner()
    if winner is not None:
        break

    #your turn
    while True:
        try:
            choice = int(input("Your move: "))
            if choice in board.available_moves():
                break
            print("That cell is taken or invalid.")

        except ValueError:
            print("Enter a number 0-8.")
    board.make_move(choice, human)
    winner = board.check_winner()
    if winner is not None:
        break


if winner == ai:
    print("Agent wins!")
elif winner == human:
    print("You win!")
else:
    print("Draw!")
