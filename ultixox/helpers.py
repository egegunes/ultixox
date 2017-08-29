def check_board(fields):
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
        field_1 = fields[WINNER[0][0]][WINNER[0][1]]
        field_2 = fields[WINNER[1][0]][WINNER[1][1]]
        field_3 = fields[WINNER[2][0]][WINNER[2][1]]

        if field_1 == field_2 == field_3:
            return field_1
