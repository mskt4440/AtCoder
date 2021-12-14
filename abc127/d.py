#
# abc127 d
#
import sys
from io import StringIO
import unittest
import bisect
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
        input = """3 2
5 1 4
2 3
1 5"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4"""
        output = """338"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
100 100 100
3 99
3 99"""
        output = """300"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000"""
        output = """10000000001"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]

    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)

    n = 0
    for b, c in BC:
        nn = min(b, N-n)
        A += [c]*nn
        n += nn

        if n >= N:
            break
    A.sort(reverse=True)

    print(sum(A[:N]))


if __name__ == "__main__":
    # unittest.main()
    resolve()
