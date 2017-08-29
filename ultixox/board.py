from helpers import check_board


class Board:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = None
        self.fields = [[None for column in range(3)] for row in range(3)]

    def __repr__(self):
        return f'Board({self.row}, {self.column})'

    def move(self, value, row, column):
        self.fields[row][column] = value

    def check(self):
        if self.value is not None:
            return self.value

        self.value = check_board(self.fields)

        return self.value

    def state(self, current=None, move=()):
        if not current:
            current = self.fields

        state = [[f for f in field] for field in current]

        if move:
            state[move[1]][move[2]] = move[0]

        return state
