#
# abc026 b
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
        input = """3
1
2
3"""
        output = """18.8495559215"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
15
2
3
7
6
9"""
        output = """508.938009881546"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    R = [int(input()) for _ in range(N)]

    R.sort(reverse=True)
    ans = 0
    flag = True
    for r in R:
        if flag:
            ans += r*r
            flag = False
        else:
            ans -= r*r
            flag = True

    print(ans*math.pi)


if __name__ == "__main__":
    # unittest.main()
    resolve()
