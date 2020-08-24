#
# abc145 c
#

import sys
from io import StringIO
import unittest
import math
import itertools


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
0 0
1 0
0 1"""
        output = """2.2761423749"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
-879 981
-866 890"""
        output = """91.9238815543"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
-406 10
512 859
494 362
-955 -475
128 553
-986 -885
763 77
449 310"""
        output = """7641.9817824387"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    R = itertools.permutations(range(N))

    all = 0
    for r in R:
        for pi in range(1, len(r)):
            all += math.sqrt((P[r[pi]][0]-P[r[pi-1]][0])**2 +
                             (P[r[pi]][1]-P[r[pi-1]][1])**2)

    n = 1
    for i in range(1, N+1):
        n *= i

    print(f"{all/n:.10f}")


if __name__ == "__main__":
    # unittest.main()
    resolve()
