#
# dp b
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
        input = """5 3
10 30 40 50 20"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
10 20 10"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 100
10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 4
40 10 20 70 80 10 20 70 80 60"""
        output = """40"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    dp = [float("inf")]*N
    dp[0] = 0
    for i in range(N):
        for j in range(K):
            if i+j+1 < N:
                dp[i+j+1] = min(dp[i+j+1], dp[i] + abs(H[i+j+1]-H[i]))

    print(dp[N-1])


if __name__ == "__main__":
    unittest.main()
    # resolve()
