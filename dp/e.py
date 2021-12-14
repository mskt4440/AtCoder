#
# dp e
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
        input = """1 1000000000
1000000000 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 15
6 5
5 6
6 4
6 6
3 5
7 2"""
        output = """17"""
        self.assertIO(input, output)


def resolve():
    N, W = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]

    dp = [[float("inf")]*(10**3*N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        w, v = WV[i-1]
        for j in range(10**3*N+1):
            dp[i][j] = dp[i-1][j]
            if j >= v:
                dp[i][j] = min(dp[i][j], dp[i-1][j-v]+w)

    ans = 10**3*N
    while dp[N][ans] > W:
        ans -= 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
