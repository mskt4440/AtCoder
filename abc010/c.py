#
# abc010 c
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

    def test_入力例1(self):
        input = """1 1 8 2 2 4
1
4 5"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1 8 2 2 6
1
4 5"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 1 8 2 2 5
1
4 5"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """7 7 1 1 3 4
3
8 1
1 7
9 9"""
        output = """YES"""
        self.assertIO(input, output)


def resolve():
    txa, tya, txb, tyb, T, V = map(int, input().split())
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    ans = "NO"
    for x, y in XY:
        m = math.sqrt((x-txa)**2 + (y-tya)**2) + \
            math.sqrt((x-txb)**2 + (y-tyb)**2)
        if m <= T*V:
            ans = "YES"
            break
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
