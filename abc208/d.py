#
# abc208 d
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

    def test_入力例_1(self):
        input = """3 2
1 2 3
2 3 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 20
1 2 6
1 3 10
1 4 4
1 5 1
2 1 5
2 3 9
2 4 8
2 5 6
3 1 5
3 2 1
3 4 7
3 5 9
4 1 4
4 2 6
4 3 4
4 5 8
5 1 2
5 2 5
5 3 6
5 4 5"""
        output = """517"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]

    dp = [[[float("inf")]*N for _ in range(N)] for _ in range(N+1)]

    for a, b, c in ABC:
        dp[0][a-1][b-1] = c

    for i in range(1, N+1):
        for a, b, c in ABC:
            for j in range(i):
                for c in range(N):
                    t = min(dp[j][a-1][c-1]+dp[k-j][c-1][b-1])

            dp[i][a-1][b-1] = min(dp[0][a-1][b-1], t)


if __name__ == "__main__":
    unittest.main()
    # resolve()
