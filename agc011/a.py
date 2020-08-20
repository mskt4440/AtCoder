#
# agc011 a
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
        input = """5 3 5
1
2
3
6
12"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 3 3
7
6
2
8
10
6"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N, C, K = map(int, input().split())
    T = []
    for _ in range(N):
        T.append(int(input()))
    T.sort()

    ans = 0
    u = 0
    s = T[N-1] + K + 1
    for t in reversed(T):
        if t + K >= s and u < C:
            u += 1
        else:
            ans += 1
            s = t
            u = 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
