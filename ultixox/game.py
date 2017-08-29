from ast import literal_eval

from player import Player
from board import Board, FieldOccupied
from helpers import check_board


class InvalidBoard(ValueError):
    pass


class Game:
    def __init__(self):
        self.boards = [[Board(row, column) for column in range(3)] for row in range(3)]
        self.status = None
        self.players = (Player(0), Player(1))
        self.turn = self.players[0]
        self.next_board = None

    def move(self, player, move):
        if self.next_board and (move[0] != self.next_board.row or move[1] != self.next_board.column):
            raise InvalidBoard(f'{self.next_board} is the only valid board to play.')

        self.boards[move[0]][move[1]].move(player, move[2], move[3])
        self.next_board = self.boards[move[2]][move[3]]

    def check(self, fields):
        self.status = check_board(fields)

    def state(self):
        return [[b.value for b in board] for board in self.boards]


if __name__ == '__main__':
    game = Game()
    while game.status is None:
        move = None
        while move is None:
            move = literal_eval(input(f'{game.turn} Move: '))

            try:
                game.move(game.turn.indicator, move)
            except (FieldOccupied, InvalidBoard):
                print("Invalid move. Try again.")
                move = None

        game.check(game.state())
        game.turn = game.players[int(not game.players.index(game.turn))]
