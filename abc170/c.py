#
# abc170 c
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
        input = """6 5
4 7 10 6 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 5
4 7 10 6 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 0"""
        output = """100"""
        self.assertIO(input, output)


def resolve():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
    else:
        P = list(map(int, input().split()))
        SP = set(P)
        ans = 0
        dif = X
        for i in range(102):
            if i in SP:
                continue
            if dif > abs(X-i):
                dif = abs(X-i)
                ans = i
        print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
