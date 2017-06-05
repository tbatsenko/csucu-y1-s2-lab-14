from btnode import BTNode


class BTree(object):
    """docstring for BTree."""
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None

    def isEmpty(self):
        if self.root == None:
            return True
        return False

    def __str__(self):
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "|   " * level
                s += str(node.value) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self.root, 0)

    def add(self, value):
        if self.root == None:
            self.root = BTNode(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if node.left == None:
            node.left = BTNode(value)
        elif node.right == None:
            node.right = BTNode(value)
