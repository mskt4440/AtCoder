#
# abc151 b
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
        input = """5 10 7
8 10 3 6"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 100 60
100 100 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 100 60
0 0 0"""
        output = """-1"""
        self.assertIO(input, output)


def resolve():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    S = sum(A)
    if (ans := max(N*M-S, 0)) > K:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
