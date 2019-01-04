from abc import ABC, abstractmethod

class PriorityQueue(ABC):
    def __init__(self):
        self.tree = []

    def __repr__(self):
        return str(self.tree)

    def __len__(self):
        return len(self.tree)

    @abstractmethod
    def comp(self, l, r):
        pass

    def swap(self, i, j):
        tmp = self.tree[i]
        self.tree[i] = self.tree[j]
        self.tree[j] = tmp

    def insert(self, c):
        cur = len(self.tree)
        self.tree.append(c)

        while cur != 0 and self.comp(self.tree[cur], self.tree[(cur-1)//2]):
            p = (cur-1)//2
            self.swap(p, cur)
            cur = (cur-1)//2

    def extract(self):
        c = self.tree[0]

        if len(self.tree) > 1:
            self.tree[0] = self.tree.pop()
        else:
            return self.tree.pop()

        cur = 0

        while cur*2+1 < len(self.tree):
            if cur*2+2 == len(self.tree) or self.comp(self.tree[cur*2+1], self.tree[cur*2+2]):
                j = cur*2+1
            else:
                j = cur*2+2

            if self.comp(self.tree[cur], self.tree[j]):
                return c

            self.swap(cur, j)
            cur = j

        return c

class MinPQ(PriorityQueue):
    def comp(self, l, r):
        return l.d[0] < r.d[0]

class MaxPQ(PriorityQueue):
    def comp(self, l, r):
        return l > r
