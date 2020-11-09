#
# abc182 c
#
import sys
from io import StringIO
from sys import float_repr_style
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
        input = """35"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """369"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6227384"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """11"""
        output = """-1"""
        self.assertIO(input, output)


def resolve():
    N = list(input())

    k = len(N)
    ans = 18
    for bit in reversed(range(1, 1 << k)):
        t = 0
        for i in range(k):
            if 1 << i & bit:
                t += int(N[i])
        if t % 3 == 0:
            ans = min(ans, k - bin(bit).count("1"))

    if ans == 18:
        ans = -1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
