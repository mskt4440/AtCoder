#
# abc149 b
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

    def test_入力例_1(self):
        input = """2 3 3"""
        output = """0 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """500000000000 500000000000 1000000000000"""
        output = """0 0"""
        self.assertIO(input, output)


def resolve():
    A, B, K = map(int, input().split())

    a = max(A-K, 0)
    b = max(B-max(K-A, 0), 0)
    print(a, b)


if __name__ == "__main__":
    # unittest.main()
    resolve()
