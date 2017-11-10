class Player:
    def __init__(self, indicator, computer=False):
        self.indicator = indicator
        self.computer = computer

    def __repr__(self):
        return f'Player {self.indicator}'

    def get_move(self, state, next_board):
        moves = next_board.available_moves
        self._minimax(next_board, 10 - len(moves), self.indicator)
        move = moves[self.index]
        return (next_board.row, next_board.column, move[0], move[1])

    def _minimax(self, board, depth, player):
        if depth is 0 or board.value is not None:
            return {
                0: depth - 10,
                1: 10 - depth,
                None: 0
            }[board.value]

        scores = [self._minimax(board.next_state(move, player), depth - 1, int(not player))
                  for move in board.available_moves]

        self.index = scores.index(max(scores)) if player is 1 else scores.index(min(scores))

        return max(scores) if player is 1 else min(scores)
