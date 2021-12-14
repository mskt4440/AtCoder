#
# abc211 d
#
import sys
from io import StringIO
import unittest
import collections


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4 5
2 4
1 2
2 3
1 3
3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
1 3
2 3
2 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 8
1 3
1 4
2 3
2 4
2 5
2 6
5 7
6 7"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    global N, G, md
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    G = [[]*N for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    D = [-1]*N
    C = [0]*N
    q = collections.deque()
    q.append(0)
    D[0] = 0
    C[0] = 1
    while q:
        p = q.pop()
        for np in G[p]:
            if D[np] != -1:
                if D[np] == D[p]+1:
                    C[np] += C[p]
                continue
            D[np] = D[p]+1
            C[np] = C[p]
            q.appendleft(np)

    print(C[N-1])


if __name__ == "__main__":
    unittest.main()
    # resolve()
