#
# abc016 a
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

    def test_入力例1(self):
        input = """1 1"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2 29"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """12 6"""
        output = """YES"""
        self.assertIO(input, output)


def resolve():
    M, D = map(int, input().split())

    if M % D:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # unittest.main()
    resolve()