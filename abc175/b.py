#
# abc175 b
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
        input = """5
4 4 9 7 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
4 5 4 3 3 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
9 4 6 1 9 6 10 6 6 8"""
        output = """39"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 1"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    L = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] == L[j] or L[j] == L[k] or L[i] == L[k]:
                    continue
                if abs(L[j] - L[k]) < L[i] < L[j] + L[k]:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
