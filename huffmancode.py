from binarytree import BinaryTreeNode
from pq import MinPQ
from collections import Counter

class HuffmanCoder:
    def __init__(self, text):
        self.text = text
        self.letter_counts = Counter(text)
        self.pq = self.create_base_pq()
        self.hufftree = self.create_huffmancode()
        self.hufftable = self.dfs()
        self.huffcode = self.hufencode()

    def __repr__(self):
        col_widths = [4, 7, 20]
        template = "{0:<%d}{1:>%d}{2:>%d}\n" % (col_widths[0], col_widths[1], col_widths[2])
        s = template.format("char", "n", "code")
        s += '-' * sum(col_widths) + '\n'

        for letter, counts in self.letter_counts.most_common(50):
            code = "".join([str(i) for i in self.hufftable[letter]])
            s += template.format(letter, counts, code)

        return s

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
    with open("long_japanese.txt") as f:
        s = f.read()
    coder = HuffmanCoder(s)
    print("Encoding Table")
    print(coder)
    print("Original character count: %d" % len(s))
    print("Original string bits: %d" % coder.original_text_bits())
    print("Encoded string bits: %d" % coder.encoded_text_bits())

