#
# abc035 c
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
        input = """5 4
1 4
2 5
3 3
1 5"""
        output = """01010"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 8
1 8
4 13
8 8
3 18
5 20
19 20
2 7
4 9"""
        output = """10110000011110000000"""
        self.assertIO(input, output)


def resolve():
    N, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(Q)]

    S = [0]*(N+1)
    for l, r in LR:
        S[l-1] += 1
        S[r] -= 1

    p = 0
    for i in range(N):
        p += S[i]
        if p % 2:
            print("1", end="")
        else:
            print("0", end="")

    print()


if __name__ == "__main__":
    # unittest.main()
    resolve()
