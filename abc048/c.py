#
# abc048 c
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
        input = """3 3
2 2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 1
1 6 1 2 0 4"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 9
3 1 4 1 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 0
5 5"""
        output = """10"""
        self.assertIO(input, output)


def resolve():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if a[i] > x:
            ans += (a[i] - x)
            a[i] = x

    for i in range(1, N):
        if a[i-1] + a[i] > x:
            ans += (a[i] + a[i-1] - x)
            a[i] = x - a[i-1]

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
