#
# abc194 d
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

    def test_入力例_1(self):
        input = """2"""
        output = """2.00000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3"""
        output = """4.50000000000"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    ans = 0
    for i in range(1, N):
        ans += N/(N-i)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
