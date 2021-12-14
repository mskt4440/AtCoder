#
# abc162 c
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
        input = """2"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """200"""
        output = """10813692"""
        self.assertIO(input, output)


def resolve():
    K = int(input())

    ans = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            for c in range(1, K+1):
                ans += functools.reduce(math.gcd, [a, b, c])
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
