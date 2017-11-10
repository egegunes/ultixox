from copy import deepcopy
from itertools import product

from helpers import check


class Board:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = None
        self.fields = [[None for column in range(3)] for row in range(3)]

    def __repr__(self):
        return f'Board({self.row}, {self.column})'

    def move(self, move, player):
        if self.fields[move[0]][move[1]] is not None:
            raise ValueError(f'{move[0]},{move[1]} on {self} is occupied by {self.fields[move[0]][move[1]]}')

        self.fields[move[0]][move[1]] = player
        self.check()

    def check(self):
        if self.value is not None:
            return self.value

        self.value = check(self.fields)

        return self.value

    def next_state(self, move, player):
        board = deepcopy(self)
        board.move(move, player)
        return board

    @property
    def available_moves(self):
        return [(row, column) for row, column in product(range(3), range(3)) if self.fields[row][column] is None]
