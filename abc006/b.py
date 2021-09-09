#
# abc006 b
#
import sys
from io import StringIO
import unittest
from unittest import async_case


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
        input = """7"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000"""
        output = """7927"""
        self.assertIO(input, output)


def resolve():
    n = int(input())
    ans = [0]*1000000

    ans[2] = 1

    if n > 2:
        for i in range(3, n):
            ans[i] = (ans[i-1]+ans[i-2]+ans[i-3]) % 10007

    print(ans[n-1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
