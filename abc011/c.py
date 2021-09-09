#
# abc011 c
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
        input = """2
1
7
15"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
1
4
2"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """300
57
121
244"""
        output = """NO"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    NG = [int(input()) for _ in range(3)]

    dp = [0]*300
    for i in range(300):
        if i+1 in NG:
            dp[i] = 0
            continue
        if i == 0 or i == 1 or i == 2:
            dp[i] = 1
        else:
            t = float("inf")
            for j in range(3):
                if dp[i-1-j] == 0:
                    continue
                t = min(t, dp[i-1-j]+1)
            dp[i] = t

    if dp[N-1] == 0 or dp[N-1] > 100:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # unittest.main()
    resolve()
