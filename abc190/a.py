#
# abcw190 a
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
        input = """2 1 0"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 0"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 1"""
        output = """Takahashi"""
        self.assertIO(input, output)


def resolve():
    A, B, C = map(int, input().split())

    if C == 0 and A > B:
        print("Takahashi")
    elif C != 0 and A >= B:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    # unittest.main()
    resolve()
