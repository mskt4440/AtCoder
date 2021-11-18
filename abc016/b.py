#
# abc016 b
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
        input = """1 0 1"""
        output = """?"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1 2"""
        output = """+"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 1 0"""
        output = """-"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """1 1 1"""
        output = """!"""
        self.assertIO(input, output)


def resolve():
    A, B, C = map(int, input().split())

    if C == A+B and C == A-B:
        print("?")
    elif C == A+B:
        print("+")
    elif C == A-B:
        print("-")
    else:
        print("!")


if __name__ == "__main__":
    # unittest.main()
    resolve()
