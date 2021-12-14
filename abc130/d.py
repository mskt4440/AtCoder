#
# abc130 d
#
import sys
from io import StringIO
import unittest
from itertools import accumulate


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
        input = """4 10
6 1 2 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
3 3 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352"""
        output = """36"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    AA = [0] + list(accumulate(A))

    ans = 0
    r = 0
    for l in range(N+1):
        while r < N and AA[r] - AA[l] < K:
            r += 1

        if AA[r] - AA[l] >= K:
            ans += N-r+1

        if r < N and r == l:
            r += 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
