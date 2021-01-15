#
# abc072 d
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
        input = """5
1 4 3 5 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """9
1 2 4 9 5 8 7 3 6"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    P = list(map(int, input().split()))

    ans = 0
    for l in range(N-1):
        for r in (l, N-1):
            if r == P[r-1]:
                P[r-1], P[r] = P[r], P[r-1]
                ans += 1
                r += 1
                break
        l = r
    else:
        if N == P[-1]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
