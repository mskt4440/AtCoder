#
# abc040 a
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
        input = """5 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """90 30"""
        output = """29"""
        self.assertIO(input, output)


def resolve():
    n, x = map(int, input().split())

    print(min(x-1, n-x))


if __name__ == "__main__":
    # unittest.main()
    resolve()
