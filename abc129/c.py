#
# abc129 c
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
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    A = set([int(input()) for _ in range(M)])
    mod = 1000000007

    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(N):
        if i+1 in A:
            continue
        if i == 0:
            dp[1] = 1
            continue
        else:
            dp[i+1] = dp[i] + dp[i-1]

    print(dp[-1] % mod)


if __name__ == "__main__":
    # unittest.main()
    resolve()
