#
# arc105 b
#
import sys
from io import StringIO
import unittest
import math
import functools


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
        input = """3
2 6 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """15
546 3192 1932 630 2100 4116 3906 3234 1302 1806 3528 3780 252 1008 588"""
        output = """42"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    print(gcd(A))


def gcd(l):
    return functools.reduce(math.gcd, l)


if __name__ == "__main__":
    # unittest.main()
    resolve()
