#
# abc110 b
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
        input = """3 2 10 20
8 15 13
16 22"""
        output = """No War"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2 -48 -1
-20 -35 -91 -23
-22 66"""
        output = """War"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 3 6 8
-10 3 1 5 -100
100 6 14"""
        output = """War"""
        self.assertIO(input, output)


def resolve():
    N, M, X, Y = map(int, input().split())
    XL = list(map(int, input().split()))
    YL = list(map(int, input().split()))

    XL.sort()
    YL.sort()

    if max(X, XL[-1]) < min(Y, YL[0]):
        print("No War")
    else:
        print("War")


if __name__ == "__main__":
    # unittest.main()
    resolve()
