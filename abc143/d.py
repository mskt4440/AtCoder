#
# abc143 d
#
import sys
from io import StringIO
import unittest
import bisect


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
3 4 2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1000 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
218 786 704 233 645 728 389"""
        output = """23"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    L = list(map(int, input().split()))

    L.sort()
    ans = 0
    for i, a in enumerate(L):
        for j, b in enumerate(L[i+1:], i+1):
            ans += bisect.bisect_left(L[j+1:], a+b)

    print(ans)


if __name__ == "__main__":
    unittest.main()
    # resolve()
