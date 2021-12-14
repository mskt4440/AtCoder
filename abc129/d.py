#
# abc129 d
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
        input = """4 6
#..#..
.....#
....#.
#.#..."""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 8
..#...#.
....#...
##......
..###..#
...#..#.
##....#.
#...#...
###.#..#"""
        output = """13"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    L = [[0]*W for _ in range(H)]
    R = [[0]*W for _ in range(H)]
    D = [[0]*W for _ in range(H)]
    U = [[0]*W for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                L[y][x] = 0
            elif x == 0:
                L[y][x] = 1
            else:
                L[y][x] = L[y][x-1] + 1

            if S[y][W-x-1] == "#":
                R[y][W-x-1] = 0
            elif x == 0:
                R[y][W-x-1] = 1
            else:
                R[y][W-x-1] = R[y][W-x] + 1

    for x in range(W):
        for y in range(H):
            if S[y][x] == "#":
                D[y][x] = 0
            elif y == 0:
                D[y][x] = 1
            else:
                D[y][x] = D[y-1][x] + 1

            if S[H-y-1][x] == "#":
                U[H-y-1][x] = 0
            elif y == 0:
                U[H-y-1][x] = 1
            else:
                U[H-y-1][x] = U[H-y][x] + 1
    ans = 0
    for y in range(H):
        for x in range(W):
            ans = max(ans, L[y][x]+R[y][x]+D[y][x]+U[y][x]-3)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
