#
# abc024 a
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
        input = """100 200 50 20
40 10"""
        output = """3500"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """400 1000 400 21
10 10"""
        output = """14000"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """400 1000 400 20
10 10"""
        output = """6000"""
        self.assertIO(input, output)


def resolve():
    A, B, C, K = map(int, input().split())
    S, T = map(int, input().split())

    D = 0
    if S+T >= K:
        D = C*(S+T)
    print(S*A+T*B-D)


if __name__ == "__main__":
    # unittest.main()
    resolve()
