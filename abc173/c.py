#
# abc173 c
#
import sys
from io import StringIO
import unittest
import copy


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
        input = """2 3 2
..#
###"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 4
..#
###"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 3
##
##"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6 6 8
..##..
.#..#.
#....#
######
#....#
#....#"""
        output = """208"""
        self.assertIO(input, output)


def resolve():
    H, W, K = map(int, input().split())
    M = [list(input()) for _ in range(H)]

    ans = 0
    for bh in range(1 << H):
        for bw in range(1 << W):
            NM = copy.deepcopy(M)
            for h in range(H):
                if bh & 1 << h:
                    NM[h] = ["R"]*W
            for w in range(W):
                if bw & 1 << w:
                    for h in range(H):
                        NM[h][w] = "R"
            if mc(NM, K):
                ans += 1

    print(ans)


def mc(M, K):
    t = 0
    for m in M:
        t += m.count("#")
    if t == K:
        return True
    return False


if __name__ == "__main__":
    # unittest.main()
    resolve()
