#
# abc003 c
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
        input = """2 2
1000 1500"""
        output = """1000.000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1
1000 1500"""
        output = """750"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 5
2604 2281 3204 2264 2200 2650 2229 2461 2439 2211"""
        output = """2820.031250000"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    R = list(map(int, input().split()))

    R.sort(reverse=True)
    T = R[0:K]
    T.sort()
    ans = 0
    for t in T:
        ans = (ans+t)/2

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
