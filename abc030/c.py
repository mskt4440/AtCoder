#
# abc030 c
#
import sys
from io import StringIO
import unittest
import bisect


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
        input = """3 4
2 3
1 5 7
3 8 12 13"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1
1 1
1
1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6 7
5 3
1 7 12 19 20 26
4 9 15 23 24 31 33"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    t = 0

    while t < B[-1]:
        ai = bisect.bisect_left(A, t)
        if ai == N:
            break
        t = A[ai]

        bi = bisect.bisect_left(B, t+X)
        if bi == M:
            break
        t = B[bi]+Y
        ans += 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
