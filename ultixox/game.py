from player import Player
from board import Board


class Game:
    def __init__(self):
        self.boards = {row: [Board(row, column) for column in range(3)] for row in range(3)}

    def move(self, piece, board_row, board_column, field_row, field_column):
        self.boards[board_row][board_column].fields[field_row][field_column].value = piece
