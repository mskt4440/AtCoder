
#
# abc198 c
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
        input = """5 15 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 11 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 4 4"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    R, X, Y = map(int, input().split())

    Z = math.sqrt(X**2+Y**2)
    print(int((Z+R-1)//R))


if __name__ == "__main__":
    # unittest.main()
    resolve()
