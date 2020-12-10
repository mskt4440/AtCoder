#
# abc028 a
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
        input = """80"""
        output = """Good"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """100"""
        output = """Perfect"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """59"""
        output = """Bad"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """95"""
        output = """Great"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    if N <= 59:
        print("Bad")
    elif N <= 89:
        print("Good")
    elif N <= 99:
        print("Great")
    else:
        print("Perfect")


if __name__ == "__main__":
    # unittest.main()
    resolve()
