#
# dp a
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
        input = """4
10 30 40 20"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
30 10 60 10 60 50"""
        output = """40"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    H = list(map(int, input().split()))

    dp = [float("inf")]*N
    dp[0] = 0

    for i in range(N-1):
        dp[i+1] = min(dp[i+1], dp[i] + abs(H[i+1]-H[i]))
        if i < N-2:
            dp[i+2] = min(dp[i+2], dp[i] + abs(H[i+2]-H[i]))

    print(dp[N-1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
