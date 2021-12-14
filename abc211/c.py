#
# abc211 c
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
        input = """chchokudai"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoderrr"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """chokudaichokudaichokudai"""
        output = """45"""
        self.assertIO(input, output)


def resolve():
    S = list(input())
    T = ["c", "h", "o", "k", "u", "d", "a", "i"]

    N = len(S)
    dp = [[0]*(N+1) for _ in range(9)]

    for i in range(9):
        for j in range(N+1):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 0
            elif S[j-1] == T[i-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    print(dp[8][N] % (10**9+7))


if __name__ == "__main__":
    # unittest.main()
    resolve()
