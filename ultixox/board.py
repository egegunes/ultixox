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
        self.fields[row][column].value = value
        self.check()

    def check(self):
        if self.value is not None:
            return self.value

        self.value = check_board(self.fields)

        return self.value
