#
# abc094 d
#
import sys
from io import StringIO, UnsupportedOperation
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
        input = """5
6 9 4 2 11"""
        output = """11 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
100 0"""
        output = """100 0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    ai = A[-1]
    tmp = ai
    aj = 0
    for a in A:
        mx = max(a, ai-a)
        if mx < tmp:
            tmp = mx
            aj = a
    print(ai, aj)


if __name__ == "__main__":
    # unittest.main()
    resolve()
