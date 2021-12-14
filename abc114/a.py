#
# abc114 a
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
        input = """5"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6"""
        output = """NO"""
        self.assertIO(input, output)


def resolve():
    X = int(input())
    if X == 7 or X == 5 or X == 3:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # unittest.main()
    resolve()
