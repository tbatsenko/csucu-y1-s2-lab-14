from btree import BTree
import random

class Bot(object):
    """docstring for Bot."""
    def __init__(self, turn):
        self.turn = turn
        decision_tree = BTree()

    def make_move(self, board):
        row = random.choice([0, 1, 2])
        col = random.choice([0, 1, 2])
        coord = (row, col)
        moveMade = False
        while not moveMade:
            if board.put(self.turn, coord):
                moveMade = True

    def make_decision(self):
        # decision_tree.root.right.value =
        pass
