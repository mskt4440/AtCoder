#
# abc037 b
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
        input = """5 2
1 3 10
2 4 20"""
        output = """10
20
20
20
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 4
2 7 22
3 5 4
6 10 1
4 4 12"""
        output = """0
22
4
12
4
1
1
1
1
1"""
        self.assertIO(input, output)


def resolve():
    N, Q = map(int, input().split())
    LRT = [list(map(int, input().split())) for _ in range(Q)]

    ans = [0]*N

    for l, r, t in LRT:
        for i in range(l-1, r):
            ans[i] = t

    print(*ans, sep="\n")


if __name__ == "__main__":
    # unittest.main()
    resolve()
