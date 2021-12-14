#
# abc195 c
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
        input = """1010"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """27182818284590"""
        output = """107730272137364"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    ans = 0
    i = 1000
    while N >= i:
        ans += N-i+1
        i *= 1000
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
