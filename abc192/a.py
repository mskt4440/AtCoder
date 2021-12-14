#
# abcw192 a
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
        input = """140"""
        output = """60"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000"""
        output = """100"""
        self.assertIO(input, output)


def resolve():
    X = int(input())

    if t := X % 100:
        print(100-t)
    else:
        print(100)


if __name__ == "__main__":
    # unittest.main()
    resolve()
