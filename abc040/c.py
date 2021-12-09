#
# abc040 c
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

    def test_入力例1(self):
        input = """4
100 150 130 120"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
100 125 80 110"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """9
314 159 265 358 979 323 846 264 338"""
        output = """310"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [float("inf")]*N
    dp[0] = 0
    for i in range(N-1):
        dp[i+1] = min(dp[i+1], dp[i]+abs(A[i+1]-A[i]))
        if i < N-2:
            dp[i+2] = min(dp[i+2], dp[i]+abs(A[i+2]-A[i]))

    print(dp[-1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
