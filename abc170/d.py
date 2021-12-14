#
# abc170 c
#
import sys
from io import StringIO
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
        input = """5
24 11 8 3 16"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 5 5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
33 18 45 28 8 19 89 86 2 4"""
        output = """5"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    C = collections.Counter(A)
    A = set(A)
    S = set()
    for a in A:
        if a in S:
            continue
        for i in range(2*a, 10**6+1, a):
            S.add(i)

    ans = 0
    for a in A:
        if C[a] != 1 or a in S:
            continue
        ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
