#
# abc163 a
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
        input = """1"""
        output = """6.28318530717958623200"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """73"""
        output = """458.67252742410977361942"""
        self.assertIO(input, output)


def resolve():
    R = int(input())

    print(2*R*math.pi)


if __name__ == "__main__":
    # unittest.main()
    resolve()
