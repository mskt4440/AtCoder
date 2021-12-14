#
# arc105 c
#
import sys
from io import StringIO
import unittest
from itertools import permutations


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
        input = """3 2
1 4 2
10 4
2 6"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1
12 345
1 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 1
1 1 1 1 1 1 1 1
100000000 1"""
        output = """700000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8 20
57 806 244 349 608 849 513 857
778 993
939 864
152 984
308 975
46 860
123 956
21 950
850 876
441 899
249 949
387 918
34 965
536 900
875 889
264 886
583 919
88 954
845 869
208 963
511 975"""
        output = """3802"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    LV = [list(map(int, input().split())) for _ in range(M)]

    P = permutations(W)
    ans = float("inf")
    for p in P:
        d = [0]*(N-1)
        f = True
        for lv in LV:
            if f == False:
                break
            l, v = lv
            tw = 0
            for i, w in enumerate(W):
                if w > v:
                    f = False
                    break
                if tw+w <= v:
                    tw += w
                else:
                    d[i] = d[i-1] + l

    print(sum(D))


if __name__ == "__main__":
    unittest.main()
    # resolve()
