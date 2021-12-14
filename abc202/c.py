#
# abc202 c
#
import sys
from io import StringIO
from typing import Collection
import unittest
import collections


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
1 2 2
3 1 2
2 3 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1
1 1 1 1
1 2 3 4"""
        output = """16"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
2 3 3
1 3 3
1 1 1"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    AC = collections.Counter(A)
    SA = set(A)
    CC = collections.Counter(C)

    ans = 0
    for k, v in CC.items():
        if B[k-1] in SA:
            ans += AC[B[k-1]]*v

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
