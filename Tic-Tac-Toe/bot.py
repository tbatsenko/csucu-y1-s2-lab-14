from btree import BTree


class Bot(object):
    """docstring for Bot."""
    def __init__(self, turn):
        self.turn = turn
        self.decision_tree = BTree(turn)

    def make_first_move(self, board):
        coord = self.decision_tree.generate_coord()
        moveMade = False
        while not moveMade:
            if board.put(self.turn, coord):
                moveMade = True
            else:
                coord = self.decision_tree.generate_coord(board)
        return board

    def make_move(self, board):
        self.decision_tree.new_generation(self.decision_tree.root)
        coord = self.decision_tree.best_move()
        moveMade = False
        while not moveMade:
            if board.put(self.turn, coord):
                moveMade = True
            else:
                coord = self.decision_tree.generate_coord(board)
        return board
