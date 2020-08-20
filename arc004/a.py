#
# arc004 a
#
import sys
from io import StringIO
import unittest
import math


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
        input = """3
1 1
2 4
4 3"""
        output = """3.605551"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
1 8
4 0
3 7
2 4
5 9
9 1
6 2
0 2
8 6
7 8"""
        output = """10.630146"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
0 0
0 100
100 0
100 100"""
        output = """141.421356"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5
3 0
1 0
0 0
4 0
2 0"""
        output = """4.000000"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """4
2 2
0 0
1 1
3 3"""
        output = """4.242641"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            d2 = (P[i][0]-P[j][0])**2 + (P[i][1]-P[j][1])**2
            ans = max(d2, ans)
    print(math.sqrt(ans))


if __name__ == "__main__":
    # unittest.main()
    resolve()
