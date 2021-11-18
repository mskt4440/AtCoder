#
# abc016 c
#
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """3 2
1 2
2 3"""
        output = """1
0
1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3
1 2
1 3
2 3"""
        output = """0
0
0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """8 12
1 6
1 7
1 8
2 5
2 6
3 5
3 6
4 5
4 8
5 6
5 7
7 8"""
        output = """4
4
4
5
2
3
4
2"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    for i, g in enumerate(G):
        tmp = set()
        for f in g:
            tmp |= set(G[f])
        tmp -= set(g)
        tmp.discard(i)
        print(len(tmp))


if __name__ == "__main__":
    # unittest.main()
    resolve()
