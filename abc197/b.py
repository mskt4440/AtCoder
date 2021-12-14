#
#  abc197 B
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
        input = """4 4 2 2
##..
...#
# .#.
.#.#"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5 1 4
#....
#####
....#"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5 4 2
.#..#
#.###
##...
#..#.
#.###"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]

    TY = S[X-1]
    TX = ""
    for i in range(H):
        TX += S[i][Y-1]

    ans = 1
    for j in range(Y+1, W+1):
        if TY[j-1] == "#":
            break
        ans += 1
    for j in range(Y-1, 0, -1):
        if TY[j-1] == "#":
            break
        ans += 1

    for i in range(X+1, H+1):
        if TX[i-1] == "#":
            break
        ans += 1
    for i in range(X-1, 0, -1):
        if TX[i-1] == "#":
            break
        ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
