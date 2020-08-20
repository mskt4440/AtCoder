#
# abc075 b
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
        input = """3 5
.....
.#.#.
....."""
        output = """11211
1#2#1
11211"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
#####
#####
#####"""
        output = """#####
#####
#####"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#..."""
        output = """#####3
#8#7##
####5#
4#65#2
#5##21
#4#310"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    A = [[0] * (W+2) for _ in range(H+2)]

    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                for i in range(y, y+3):
                    for j in range(x, x+3):
                        A[i][j] += 1

    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                print("#", end="")
            else:
                print(A[y+1][x+1], end="")
        print()


if __name__ == "__main__":
    # unittest.main()
    resolve()
