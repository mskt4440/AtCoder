#
# abc073 c
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
        input = """3
6
2
6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
2
5
5
2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
12
22
16
22
18
12"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    AM = {}
    for a in A:
        AM.setdefault(a, 0)
        AM[a] += 1

    ans = 0
    for v in AM.values():
        if v % 2 != 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
