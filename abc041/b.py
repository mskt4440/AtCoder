#
# abc041 b
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
        input = """2 3 4"""
        output = """24"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """10000 1000 100"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """100000 1 100000"""
        output = """999999937"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """1000000000 1000000000 1000000000"""
        output = """999999664"""
        self.assertIO(input, output)


def resolve():
    A, B, C = map(int, input().split())

    print(A*B*C % (10**9+7))


if __name__ == "__main__":
    # unittest.main()
    resolve()
