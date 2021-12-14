#
# abc112 a
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
        input = """1"""
        output = """Hello World"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
3
5"""
        output = """8"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    if N == 1:
        print("Hello World")
    else:
        A = int(input())
        B = int(input())
        print(A+B)


if __name__ == "__main__":
    # unittest.main()
    resolve()
