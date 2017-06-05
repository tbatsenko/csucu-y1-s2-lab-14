class Board(object):
    """docstring for Board."""
    EMPTY_CELL = " "

    # O_CELL = 1
    # X_CELL = 2
    # X_winns = 3
    # O_winns = 4
    # DRAW = 5
    # NOT_ENDED = 6
    COMBINATIONS = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                    ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 2), (2, 2)),
                    ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),
                    ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))

    def __init__(self):
        self._field = [[Board.EMPTY_CELL for i in range(3)] for j in range(3)]
        self._lastMove = None
        print(self._field)

    def put(self, turn, coord):
        """put an X or O to the board"""
        row = coord[0]
        col = coord[1]
        if self._field[row][col] == Board.EMPTY_CELL:
            print(self._field[0][0])
            self._field[row][col] = turn
            self._lastMove = (turn, coord)
            return True
        else:
            return False

    def check_winner(self):
        """check if there is a winner"""
        def get_value(coord):
            return self._field[coord[0]][coord[1]]
        counter = 0
        for comb in Board.COMBINATIONS:
            if get_value(comb[0]) == get_value(comb[1]) == get_value(comb[2]) != Board.EMPTY_CELL:
                counter += 1
                winner = get_value(comb[0])
        if counter > 0:
            return winner
        return None
