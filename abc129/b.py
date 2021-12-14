#
# abc129 b
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
        input = """3
1 2 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 3 1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
27 23 76 2 3 5 62 52"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    W = list(map(int, input().split()))

    ans = float("inf")
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i])-sum(W[i:])))

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
