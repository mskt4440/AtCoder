#
# abc191 d
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
        input = """0.2 0.8 1.1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 100 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """42782.4720 31949.0192 99999.99"""
        output = """31415920098"""
        self.assertIO(input, output)


def resolve():
    X, Y, R = map(int, input())


if __name__ == "__main__":
    unittest.main()
    # resolve()
