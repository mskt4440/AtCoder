#
# abc153 e
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
        input = """9 3
8 3
4 2
2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 6
1 1
2 3
3 9
4 27
5 81
6 243"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9999 10
540 7550
691 9680
700 9790
510 7150
415 5818
551 7712
587 8227
619 8671
588 8228
176 2461"""
        output = """139815"""
        self.assertIO(input, output)


def resolve():
    H, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [[float("inf")]*(H+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        a, b = AB[i]
        for j in range(H+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            dp[i+1][min(j+a, H)] = min(dp[i+1][min(j+a, H)], dp[i+1][j]+b)
    print(dp[N][H])


if __name__ == "__main__":
    unittest.main()
    # resolve()
