#
# abc031 a
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
        input = """31 87"""
        output = """2784"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """101 65"""
        output = """6666"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3 3"""
        output = """12"""
        self.assertIO(input, output)


def resolve():
    A, D = map(int, input().split())
    print(max((A+1)*D, A*(D+1)))


if __name__ == "__main__":
    # unittest.main()
    resolve()
