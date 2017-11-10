def check(board):
    WINNERS = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    )

    for WINNER in WINNERS:
        if (board[WINNER[0][0]][WINNER[0][1]]
                == board[WINNER[1][0]][WINNER[1][1]]
                == board[WINNER[2][0]][WINNER[2][1]]):
            return board[WINNER[0][0]][WINNER[0][1]]
