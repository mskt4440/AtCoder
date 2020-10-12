#
# hhkb2020 c
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
        input = """4
1 1 0 2"""
        output = """0
0
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
5 4 3 2 1 0 7 7 6 6"""
        output = """0
0
0
0
0
6
6
6
8
8"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    P = list(map(int, input().split()))

    F = [0]*200001
    ans = 0
    for p in P:
        F[p] += 1
        while F[ans]:
            ans += 1
        print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
