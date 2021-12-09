#
# abc040 b
#
import sys
from io import StringIO
import unittest
import math


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
        input = """26"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """41"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """100000"""
        output = """37"""
        self.assertIO(input, output)


def resolve():
    n = int(input())

    ans = float("inf")
    for i in range(1, int(math.sqrt(n))+1):
        ans = min(ans, n % i+abs(n//i-i))

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
