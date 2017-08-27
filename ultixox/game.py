from player import Player
from board import Board
from helpers import check_board


class Game:
    def __init__(self):
        self.boards = {row: [Board(row, column) for column in range(3)] for row in range(3)}
        self.status = None

    def move(self, value, board_row, board_column, field_row, field_column):
        self.boards[board_row][board_column].move(value, field_row, field_column)
        if self.boards[board_row][board_column].value is not None:
            self.check()

    def check(self):
        self.status = check_board(self.boards)

