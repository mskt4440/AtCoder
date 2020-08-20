#
# abc057 c
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
        input = """10000"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000003"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9876543210"""
        output = """6"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    ans = float("inf")
    for a in range(1, int(math.sqrt(N))+1):
        if N % a == 0:
            b = N // a
            ans = min(ans, len(str(b)))
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
