"""
Pseudo codigo

Class environment
__init__()
is_empty(i, j)
reward(symbol)
get_state()
game_over()
draw_board()

"""
import numpy as np


LENGTH=3


class Environment:
    def __init_(self, LENGTH):
        self.board  = np.zero((LENGTH, LENGTH))
        self.x = -1
        self.o = 1
        self.winner = None
        self.ended  = False
        self.num_estates = 3**(LENGTH*LENGTH)

    def is_empty(self. i, j):
        return self.boarf[i, j] == 0

    def reward(self, sym):
        if not self.game_over():
            return 0
        return 1 if self.winner == sym else 0

    def get_state(self):
        k = 0
        h = 0
        for i in range(LENGTH):
            for  j in range(LENGTH):
                if self.board[i, j] == 0):
                    v = 0
                elif self.board[[i, j] == self.x:
                    v = 1
                elif self.board[i, l] == self.o:
                    v = 2
                h += (3**k)*v
                k +1

    return h
