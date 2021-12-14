#
# abcw194 a
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
        input = """10 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 0"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    if A+B >= 15 and B >= 8:
        print(1)
    elif A+B >= 10 and B >= 3:
        print(2)
    elif A+B >= 3:
        print(3)
    else:
        print(4)


if __name__ == "__main__":
    # unittest.main()
    resolve()
