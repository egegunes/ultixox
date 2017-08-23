class Field:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = None

    def __repr__(self):
        return f'Field({self.row}, {self.column})'


class Board:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.fields = {row: [Field(row, column) for column in range(3)] for row in range(3)}

    def __repr__(self):
        return f'Board({self.row}, {self.column})'

