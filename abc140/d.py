#
# abc140 d
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
        input = """6 1
LRLRRL"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """13 3
LRRLRLRRLRLLR"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 1
LLLLLRRRRR"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """9 2
RRRLRLRLL"""
        output = """7"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    S = input()

    a = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            a += 1
    print(N-1-max(a-K*2, 0))


if __name__ == "__main__":
    # unittest.main()
    resolve()
