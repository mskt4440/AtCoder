#
# abc059 c
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
        input = """4
1 -3 1 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
3 -6 4 -5 7"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
-1 4 3 2 -5 4"""
        output = """8"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    # n = odd : plus
    ansa = 0
    sa = 0
    for i in range(N):
        sa += A[i]
        if i % 2 == 0:
            if sa >= 0:
                ansa += abs(sa) + 1
                sa = -1
        else:
            if sa <= 0:
                ansa += abs(sa) + 1
                sa = 1

    # n = even : plus
    ansb = 0
    sb = 0
    for i in range(N):
        sb += A[i]
        if i % 2 == 0:
            if sb <= 0:
                ansb += abs(sb) + 1
                sb = +1
        else:
            if sb >= 0:
                ansb += abs(sb) + 1
                sb = -1

    print(min(ansa, ansb))


if __name__ == "__main__":
    # unittest.main()
    resolve()
