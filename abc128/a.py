#
# abc128 a
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
        input = """1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """32 21"""
        output = """58"""
        self.assertIO(input, output)


def resolve():
    A, P = map(int, input().split())

    print((A*3+P)//2)


if __name__ == "__main__":
    # unittest.main()
    resolve()
