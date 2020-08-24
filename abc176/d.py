#
# abc176 d
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
        input = """4 4
1 1
4 4
..#.
..#.
.#..
.#.."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 4
4 1
.##.
####
####
.##."""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 4
2 2
3 3
....
....
....
...."""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4 5
1 2
2 5
#.###
# .
#..##
# ..##"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    if abs(Dh-Ch) <= 2 and abs(Dw-Cw) <= 2:
        ans = 1


if __name__ == "__main__":
    unittest.main()
