#
# agc013 a
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
        input = """6
1 2 3 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
1 2 1 2 1 2 1 2 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1 2 3 2 1 999999999 1000000000"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 1
    flag = 0
    for i in range(1, N):
        if flag == 0:
            if A[i-1] < A[i]:
                flag = 1
            elif A[i-1] > A[i]:
                flag = -1
        elif flag == 1:
            if A[i-1] > A[i]:
                ans += 1
                flag = 0
        else:
            if A[i-1] < A[i]:
                ans += 1
                flag = 0
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
