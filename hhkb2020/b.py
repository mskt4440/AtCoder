#
# hhkb2020 b
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
        input = """2 3
..#
#.."""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2
.#
#."""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for y in range(H):
        for x in range(W):
            if S[y][x] == ".":
                if x < W-1 and S[y][x+1] == ".":
                    ans += 1
                if y < H-1 and S[y+1][x] == ".":
                    ans += 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
