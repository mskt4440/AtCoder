#
# abc165 d
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
        input = """5 7 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11 10 9"""
        output = """9"""
        self.assertIO(input, output)


def resolve():
    A, B, N = map(int, input().split())

    if N > B-1:
        print(math.floor(A*(B-1)/B))
    else:
        print(math.floor(A*N/B))


if __name__ == "__main__":
    # unittest.main()
    resolve()
