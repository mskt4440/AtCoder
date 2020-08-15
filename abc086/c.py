#
# abc086 c
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
        input = """2
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    t = [[0, 0, 0]]
    for _ in range(N):
        t.append(list(map(int, input().split())))

    ans = "Yes"
    for i in range(1, N+1):
        s = t[i][0] - t[i-1][0]
        xd = abs(t[i][1] - t[i-1][1])
        yd = abs(t[i][2] - t[i-1][2])
        d = xd + yd
        if d > s or s % 2 != d % 2:
            ans = "No"
            break
    print(ans)


if __name__ == "__main__":
    unittest.main()
    # resolve()
