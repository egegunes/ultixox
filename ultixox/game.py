from player import Player
from board import Board
from helpers import check_board


class Game:
    def __init__(self):
        self.boards = [[Board(row, column) for column in range(3)] for row in range(3)]
        self.status = None

    def move(self, player, move):
        self.boards[move[0]][move[1]].move(player, move[2], move[3])

    def check(self):
        self.status = check_board(self.boards)
