#
# abc039 d
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

    def test_入力例1(self):
        input = """4 4
##..
##..
..##
..##"""
        output = """possible
#...
....
....
...#"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 4
###.
####
..##
..##"""
        output = """possible
##..
....
...#
...#"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 4
###.
##.#
..##
..##"""
        output = """impossible"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    M = [["#"]*W for _ in range(H)]
    ans = "possible"

    dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                continue
            for i in range(9):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or W <= nx or ny < 0 or H <= ny:
                    continue
                M[ny][nx] = "."

    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                for i in range(9):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if nx < 0 or W <= nx or ny < 0 or H <= ny:
                        continue
                    if M[ny][nx] == "#":
                        break
                else:
                    ans = "impossible"
        if ans == "impossible":
            break

    print(ans)
    if ans == "possible":
        for m in M:
            print(*m, sep="")


if __name__ == "__main__":
    # unittest.main()
    resolve()
