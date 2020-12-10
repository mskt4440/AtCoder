#
# abc028 c
#
import sys
from io import StringIO
import unittest
from itertools import combinations


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
        input = """1 2 3 4 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 2 3 5 8"""
        output = """14"""
        self.assertIO(input, output)


def resolve():
    L = list(map(int, input().split()))
#    C = combinations(L, 3)
#    S = []
#    for c in C:
#        S.append(sum(c))
#    SS = list(set(S))
#    SS.sort(reverse=True)
#    print(SS[2])
    print(max(L[0]+L[3]+L[4], L[1]+L[2]+L[4]))


if __name__ == "__main__":
    # unittest.main()
    resolve()
