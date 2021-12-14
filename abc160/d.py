#
# abc160 d
#
import sys
from io import StringIO
import unittest
from collections import deque


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
        input = """5 2 4"""
        output = """5
4
1
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1 3"""
        output = """3
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 3 7"""
        output = """7
8
4
2
0
0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 4 8"""
        output = """10
12
10
8
4
1
0
0
0"""
        self.assertIO(input, output)


def resolve():
    N, X, Y = map(int, input().split())

    ans = [0]*(N-1)
    for i in range(N):
        for j in range(i+1, N):
            d = min(abs(i-j), abs(i-(X-1))+abs(j-(Y-1)) +
                    1, abs(i-(Y-1))+abs(j-(X-1))+1)
            ans[d-1] += 1

    for a in ans:
        print(a)


if __name__ == "__main__":
    # unittest.main()
    resolve()
