#
# abc113 b
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
        input = """2
12 5
1000 2000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
21 -11
81234 94124 52141"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    dmin = float('inf')
    for i in range(N):
        d = abs(A - (T - H[i] * 0.006))
        if d < dmin:
            dmin = d
            ans = i+1
    print(ans)


if __name__ == "__main__":
    unittest.main()
    # resolve()
