#
# abc036 a
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
        input = """12 36"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """12 100"""
        output = """9"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    print((B+A-1)//A)


if __name__ == "__main__":
    # unittest.main()
    resolve()
