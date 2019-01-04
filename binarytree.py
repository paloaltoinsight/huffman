class BinaryTreeNode:
    def __init__(self, d, l=None, r=None):
        self.d = d
        self.l = l
        self.r = r
        self.visited = False

    def __repr__(self):
        return str(self.d) + "__" + str(self.l) + "-" + str(self.r)
