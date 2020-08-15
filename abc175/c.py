#
# abc175 c
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
        input = """6 2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 4 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 1 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1000000000000000 1000000000000000 1000000000000000"""
        output = """1000000000000000"""
        self.assertIO(input, output)


def resolve():
    X, K, D = map(int, input().split())
    s = abs(X) // D
    if K < s:
        ans = abs(X)-K*D
    else:
        if (K - s) % 2 == 0:
            ans = abs(abs(X)-s*D)
        else:
            ans = abs(abs(X)-s*D - D)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
