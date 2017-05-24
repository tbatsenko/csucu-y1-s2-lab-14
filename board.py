class Board(object):
    """docstring for Board."""
    EMPTY_CELL = 0
    O_CELL = 1
    X_CELL = 2
    X_winns = 3
    O_winns = 4
    DRAW = 5
    NOT_ENDED = 6
    COMBINATIONS = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                    ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 2), (2, 2)),
                    ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),
                    ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))

    def __init__(self):
        self._field = [[EMPTY_CELL]*3]*3

    def put(self, turn, coord):
        if self._field[coord[0][1]] == EMPTY_CELL:
            self._field[coord[0][1]].append(turn)
            return True
        else:
            return False

    def check_winner(self):
        def get_value(coord):
            return self._field[coord[0]][coord[1]]
        couter = 0
        for comb in COMBINATIONS:
            if get_value(comb[0]) == get_value(comb[1]) == get_value(comb[2]) != EMPTY_CELL:
                counter += 1
                winner = get_value(comb[0])
        if counter > 0:
            return winner
        return NOT_ENDED


if __name__ = "__main__":
