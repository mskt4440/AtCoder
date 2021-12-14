#
# abc099 c
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
        input = """127"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """44852"""
        output = """16"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    dp = [N]*(N+1)
    dp[0] = 0

    for i in range(N):
        for j in range(1, 7):
            if (n := i+6**j) > N:
                break
            dp[n] = min(dp[n], dp[i]+1)

        for j in range(1, 6):
            if (n := i+9**j) > N:
                break
            dp[n] = min(dp[n], dp[i]+1)

        dp[i+1] = min(dp[i+1], dp[i]+1)

    print(dp[N])


if __name__ == "__main__":
    # unittest.main()
    resolve()
