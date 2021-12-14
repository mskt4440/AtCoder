#
# abc146 d
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
        input = """3
1 2
2 3"""
        output = """2
1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
1 2
2 3
2 4
2 5
4 7
5 6
6 8"""
        output = """4
1
2
3
4
1
1
2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 2
1 3
1 4
1 5
1 6"""
        output = """5
1
2
3
4
5"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append((b-1, i))
        G[b-1].append((a-1, i))

    F = [False]*N
    E = [-1]*(N-1)
    q = deque()
    q.append([0, 0])
    F[0] = True
    n = 0
    while q:
        p, pc = q.popleft()
        nc = 1
        for np, ni in G[p]:
            if F[np]:
                continue
            if nc == pc:
                nc += 1
            E[ni] = nc
            q.append([np, nc])
            F[np] = True
            n = max(n, nc)
            nc += 1

    print(max(E))
    for e in E:
        print(e)


if __name__ == "__main__":
    # unittest.main()
    resolve()
