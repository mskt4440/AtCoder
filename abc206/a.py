#
# abc206 a
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
        input = """180"""
        output = """Yay!"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """200"""
        output = """:("""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """191"""
        output = """so-so"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    t = math.floor(N*1.08)
    if t < 206:
        print("Yay!")
    elif t == 206:
        print("so-so")
    else:
        print(":(")


if __name__ == "__main__":
    # uhittest.main()
    resolve()
