#
# abc031 b
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
        input = """300 400
3
240
350
480"""
        output = """60
0
-1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """50 80
5
10000
50
81
80
0"""
        output = """-1
0
-1
0
50"""
        self.assertIO(input, output)


def resolve():
    L, H = map(int, input().split())
    N = int(input())
    A = [int(input()) for _ in range(N)]

    for a in A:
        if a < L:
            print(L-a)
        elif L <= a <= H:
            print(0)
        else:
            print(-1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
