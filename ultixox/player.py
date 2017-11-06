class Player:
    def __init__(self, indicator, computer=False):
        self.indicator = indicator
        self.computer = computer

    def __repr__(self):
        return f'Player {self.indicator}'

    def get_move(self, state, next_board):
        import random
        return (next_board.row, next_board.column, random.randint(0, 2), random.randint(0, 2))
