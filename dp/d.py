#
# dp d
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
        input = """3 8
3 30
4 50
5 60"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 9
2 3
1 2
3 6
2 1
1 3
5 85"""
        output = """94"""
        self.assertIO(input, output)


def resolve():
    N, W = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0]*(W+1) for _ in range(N+1)]
    for i, wv in enumerate(WV):
        w, v = wv[0], wv[1]
        for j in range(1, W+1):
            dp[i+1][j] = dp[i][j]
            if w <= j:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-w] + v)
    print(dp[N][W])


if __name__ == "__main__":
    unittest.main()
    # resolve()
