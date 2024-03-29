#
# abc034 b
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
        input = """100"""
        output = """99"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """123456789"""
        output = """123456790"""
        self.assertIO(input, output)


def resolve():
    n = int(input())

    if n % 2:
        print(n+1)
    else:
        print(n-1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
