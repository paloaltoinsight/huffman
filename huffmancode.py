import sys
from binarytree import BinaryTreeNode
from pq import MinPQ

class HuffmanCoder:
    def __init__(self, text):
        self.text = text
        self.letter_counts = self.create_lettercounts()
        self.pq = self.create_base_pq()
        self.hufftree = self.create_huffmancode()
        self.hufftable = self.dfs()
        self.huffcode = self.hufencode()

    def __repr__(self):
        template = "{0:<4}{1:>4}{2:>8}\n"
        s = template.format("char", "n", "code")
        s += '-' * 16 + '\n'

        for letter, counts in self.letter_counts.items():
            code = "".join([str(i) for i in self.hufftable[letter]])
            s += template.format(letter, counts, code)

        return s

    def create_lettercounts(self):
        letter_counts = dict()

        for c in self.text:
            if c in letter_counts:
                letter_counts[c] += 1
            else:
                letter_counts[c] = 1

        return letter_counts

    def create_base_pq(self):
        q = MinPQ()
        for letter, n in self.letter_counts.items():
            n = BinaryTreeNode((n, letter))
            q.insert(n)

        return q

    def create_huffmancode(self):
        while len(self.pq) > 1:
            x = self.pq.extract()
            y = self.pq.extract()
            combined_score = x.d[0] + y.d[0]
            z = BinaryTreeNode((combined_score, None), x, y)
            self.pq.insert(z)

        return self.pq.extract()

    def dfs(self):
        encoding_table = {}
        s = [self.hufftree]
        prev = {}
        prev[self.hufftree] = None
        while len(s) > 0:
            v = s.pop()
            if not v.visited:
                v.visited = True

                if v.d[1]:
                    cur = v
                    path = []
                    while prev[cur]:
                        path.append(prev[cur][1])
                        cur = prev[cur][0]
                    path.reverse()
                    encoding_table[v.d[1]] = path

                if v.r:
                    s.append(v.r)
                    prev[v.r] = (v, 1)
                if v.l:
                    s.append(v.l)
                    prev[v.l] = (v, 0)

        return encoding_table

    def hufencode(self):
        encoding = [self.hufftable[c] for c in self.text]
        return "".join([str(item) for sublist in encoding for item in sublist])

    def original_text_bits(self):
        return len(self.text.encode("utf-8")) * 8

    def encoded_text_bits(self):
        return len(self.huffcode)

if __name__ == '__main__':
    s = "effervescence"
    coder = HuffmanCoder(s)
    print("Encoding Table")
    print(coder)
    print("Original string:", s)
    print("Encoded string:", coder.huffcode)
    print("Original string bits: %d" % coder.original_text_bits())
    print("Encoded string bits: %d" % coder.encoded_text_bits())

