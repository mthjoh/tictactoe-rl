import numpy as np

class QAgent:
    def __init__(self, epsilon=0.9, alpha=0.1, gamma=0.9):
        self.Q = {} # the table: (state, move) -> value
        self.epsilon = epsilon # exploration rate
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor

    def get_Q(self, state, move):
        return self.Q.get((state, move), 0.0)

    def choose_move(self, state, available_moves):
        if np.random.rand() < self.epsilon:
            return np.random.choice(available_moves) # explore
        Qs = [self.get_Q(state, m) for m in available_moves] # exploit:
        max_Q = max(Qs)
        best = [m for m, q in zip(available_moves, Qs) if q == max_Q]
        return np.random.choice(best)
    
    def update(self, state, move, reward, next_state, next_moves):
        old_Q = self.get_Q(state, move)
        if next_moves:
            future = max(self.get_Q(next_state, m) for m in next_moves)
        else:
            future = 0.0
        target = reward + self.gamma * future
        self.Q[(state, move)] = old_Q + self.alpha * (target - old_Q)

    def decay_epsilon(self, factor=0.99995, minimum=0.05):
        self.epsilon = max(self.epsilon * factor, minimum)
    

