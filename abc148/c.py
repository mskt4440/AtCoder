#
# abc148 c
#
import sys
from io import StringIO
import unittest
from math import gcd


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
        input = """2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123 456"""
        output = """18696"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 99999"""
        output = """9999900000"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    print(A*B//gcd(A, B))


if __name__ == "__main__":
    # unittest.main()
    resolve()
