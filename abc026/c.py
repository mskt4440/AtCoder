#
# abc026 c
#
import sys
from io import StringIO
from typing import get_args
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
        input = """5
1
1
1
1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """7
1
1
2
2
3
3"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6
1
2
3
3
2"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """10
1
2
3
4
5
6
7
8
9"""
        output = """1023"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    B = [int(input()) for _ in range(N-1)]

    G = [[] for _ in range(N)]
    for i, b in enumerate(B):
        G[b-1].append(i+1)

    dp = [0]*N
    for i in range(N-1, -1, -1):
        if len(G[i]) == 0:
            dp[i] = 1
            continue
        mx = 0
        mn = float('inf')
        for j in G[i]:
            mx = max(mx, dp[j])
            mn = min(mn, dp[j])
        dp[i] = mx + mn + 1

    print(dp[0])


def resolve_dfs():
    N = int(input())
    B = [int(input()) for _ in range(N-1)]

    global G
    G = [[] for _ in range(N)]
    for i, b in enumerate(B):
        G[b-1].append(i+1)

    print(dfs(0))


def dfs(n):
    if len(G[n]) == 0:
        return 1

    mx = 0
    mn = float('inf')
    for i in G[n]:
        s = dfs(i)
        mx = max(mx, s)
        mn = min(mn, s)
    return mx + mn + 1


if __name__ == "__main__":
    unittest.main()
    # resolve()
