#
# abc020 b
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
        input = """1 23"""
        output = """246"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """999 999"""
        output = """1999998"""
        self.assertIO(input, output)


def resolve():
    A, B = input().split()
    print(int(A+B)*2)


if __name__ == "__main__":
    # unittest.main()
    resolve()
