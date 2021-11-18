#
# abc020 a
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
        input = """1"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2"""
        output = """chokudai"""
        self.assertIO(input, output)


def resolve():
    Q = int(input())
    if Q == 1:
        print("ABC")
    else:
        print("chokudai")


if __name__ == "__main__":
    # unittest.main()
    resolve()
