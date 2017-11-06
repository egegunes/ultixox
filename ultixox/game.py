from ast import literal_eval

from player import Player
from board import Board
from helpers import check_board


class Game:
    def __init__(self, players):
        self.players = players
        self.turn = self.players[0]
        self.boards = [[Board(row, column) for column in range(3)] for row in range(3)]
        self.status = None
        self.next_board = None

    def move(self, player, move):
        if self.next_board and (move[0] != self.next_board.row or move[1] != self.next_board.column):
            raise ValueError(f'{self.next_board} is the only valid board to play.')

        self.boards[move[0]][move[1]].move(player, move[2], move[3])
        self.next_board = self.boards[move[2]][move[3]]
        print(f'Next board: {self.next_board}')

    def check(self, fields):
        self.status = check_board(fields)

    def state(self):
        return [[b.value for b in board] for board in self.boards]


if __name__ == '__main__':
    human = Player(0)
    computer = Player(1, computer=True)
    game = Game((human, computer))
    while game.status is None:
        move = None
        while move is None:
            if game.turn is human:
                move = literal_eval(input(f'{game.turn} Move: '))
            else:
                move = computer.get_move(game.state, game.next_board)
                print(f'Computer: {move}')

            try:
                game.move(game.turn.indicator, move)
            except ValueError as e:
                print(e)
                move = None

        game.check(game.state())
        game.turn = game.players[int(not game.players.index(game.turn))]
