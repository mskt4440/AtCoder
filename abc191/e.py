#
# abc191 e
#
import sys
from io import StringIO
import unittest
from collections import deque


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
        input = """4 4
1 2 5
2 3 10
3 1 15
4 3 20"""
        output = """30
30
30
-1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 6
1 2 5
1 3 10
2 4 5
3 4 10
4 1 10
1 1 10"""
        output = """10
20
30
20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 7
1 2 10
2 3 30
1 4 15
3 4 25
3 4 20
4 3 20
4 3 30"""
        output = """-1
-1
40
40"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]

    G = [[] for _ in range(N+1)]
    for a, b, c in ABC:
        G[a].append([b, c])

    for i in range(1, N+1):
        S = i
        T = 0

        q = deque()
        q.append([S, 0])
        while q:
            p, t = q.pop()
            T += t
            if p == S and T != 0:
                break
            for np, nt in G[p]:
                if np == S:
                    q.append([np, T+nt])
                    break
                q.append([np, T+nt])
        print(T)


if __name__ == "__main__":
    unittest.main()
    # resolve()
