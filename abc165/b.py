#
# abc165 b
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

    def test_入力例_1(self):
        input = """103"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000000000000"""
        output = """3760"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1333333333"""
        output = """1706"""
        self.assertIO(input, output)


def resolve():
    X = int(input())

    ans = 0
    t = 100
    while t < X:
        t += t//100
        ans += 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
