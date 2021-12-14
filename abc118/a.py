#
# abc118 a
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
        input = """4 12"""
        output = """16"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 20"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    if B % A:
        print(B-A)
    else:
        print(A+B)


if __name__ == "__main__":
    # unittest.main()
    resolve()
