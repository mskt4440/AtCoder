#
# abc014 b
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
        input = """4 5
1 10 100 1000"""
        output = """101"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """20 1048575
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"""
        output = """210"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 0
1000 1000 1000 1000"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    n, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for i, a in enumerate(A):
        if 1 << i & X:
            ans += a
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
