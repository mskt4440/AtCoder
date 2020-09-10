#
# smbc2019 c
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
        input = """615"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """217"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    X = int(input())

    n = X // 100
    r = X % 100
    if 0 <= r <= 5*n:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    # unittest.main()
    resolve()
