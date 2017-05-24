from board import Board


class Player(object):
    """docstring for Player."""
    def __init__(self, turn):
        self.turn = turn

    def put(self, board, coord):
        board.put(self.turn, coord)
