#
# abc039 b
#
import sys
from io import StringIO
import unittest
import math


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
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """981506241"""
        output = """177"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """390625"""
        output = """25"""
        self.assertIO(input, output)


def resolve():
    X = int(input())

    print(int(math.sqrt(math.sqrt(X))))


if __name__ == "__main__":
    # unittest.main()
    resolve()
