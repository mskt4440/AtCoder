#
# abc160 b
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
        input = """1024"""
        output = """2020"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000"""
        output = """2000000000"""
        self.assertIO(input, output)


def resolve():
    X = int(input())

    print(X//500*1000 + (X % 500)//5*5)


if __name__ == "__main__":
    # unittest.main()
    resolve()
