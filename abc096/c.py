#
# abc096 c
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
        input = """3 3
.#.
###
.#."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##."""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    S = [["."] * (W+2) for _ in range(H+2)]
    for i in range(H):
        S[i+1][1:W+1] = list(".") + list(input())

    ans = "Yes"
    for i in range(1, H+2):
        for j in range(1, W+2):
            if S[i][j] == "#":
                if S[i-1][j] == "." and S[i][j-1] == "." and S[i][j+1] == "." and S[i+1][j] == ".":
                    ans = "No"
                    break

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
