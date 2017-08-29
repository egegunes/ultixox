from ast import literal_eval

from player import Player
from board import Board, FieldOccupied
from helpers import check_board


class Game:
    def __init__(self):
        self.boards = [[Board(row, column) for column in range(3)] for row in range(3)]
        self.status = None
        self.players = (Player(0), Player(1))
        self.turn = self.players[0]

    def move(self, player, move):
        self.boards[move[0]][move[1]].move(player, move[2], move[3])

    def check(self):
        self.status = check_board(self.boards)


if __name__ == '__main__':
    game = Game()
    while game.status is None:
        move = None
        while move is None:
            move = literal_eval(input(f'{game.turn} Move: '))

            try:
                game.move(game.turn.indicator, move)
            except FieldOccupied:
                print("Invalid move. Try again.")
                move = None

        game.turn = game.players[int(not game.players.index(game.turn))]
