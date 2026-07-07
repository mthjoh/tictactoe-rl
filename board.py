import numpy as np

class Board:
    def __init__(self):
        self.state = np.zeros(9, dtype=int)  # 9 cells: 0=empty, 1=X, -1=O

    def available_moves(self):
        return [i for i in range(9) if self.state[i] == 0]
    
    def make_move(self, position, player):
        self.state[position] = player

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                 (0, 4, 8), (2, 4, 6)]             # diagonals
        for a, b, c in lines:
            total = self.state[a] + self.state[b] + self.state[c]
            if total == 3:
                return 1 # X wins
            if total == -3:
                return -1 # O wins
        if len(self.available_moves()) == 0:
            return 0  #draw
        return None # game still going
    
    def show(self):
        symbols = {0: '.', 1: 'X', -1: 'O'}
        for row in range(3):
            print(' '.join(symbols[self.state[row*3 + col]] for col in range(3)))
        print()
