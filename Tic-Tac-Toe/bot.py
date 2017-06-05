from btree import BTree
import random

class Bot(object):
    """docstring for Bot."""
    def __init__(self, turn):
        self.turn = turn
        decision_tree = BTree()

    @staticmethod
    def generate_coord():
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        return (row, col)

    def make_move(self, board):
        coord = self.generate_coord()
        moveMade = False
        while not moveMade:
            if board.put(self.turn, coord):
                moveMade = True
            else:
                coord = self.generate_coord()


    def make_decision(self, board, coord1, coord2):
        # decision_tree.root.right.value =
        pass
