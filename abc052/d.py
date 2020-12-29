#
# abc052 d
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
        input = """4 2 5
1 2 5 7"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 1 100
40 43 45 105 108 115 124"""
        output = """84"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 1 2
24 35 40 68 72 99 103"""
        output = """12"""
        self.assertIO(input, output)


def resolve():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))

    dp = [float("inf")] * N
    dp[0] = 0
    for i in range(N-1):
        dp[i+1] = dp[i] + min(A*abs(X[i+1]-X[i]), B)

    print(dp[N-1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
