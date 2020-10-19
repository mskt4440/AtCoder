#
# abc125 d
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
-10 5 -4"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
10 -4 -8 -11 3"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11
-1000000000 1000000000 -1000000000 1000000000 -1000000000 0 1000000000 -1000000000 1000000000 -1000000000 1000000000"""
        output = """10000000000"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    ans = 0
    for i in range(1, N, 2):
        if A[i-1] < 0 and A[i] < 0:
            ans += -1*(A[i-1]+A[i])
        elif A[i-1] < 0 and A[i] >= 0:
            ans += max(abs(A[i-1]), abs(A[i])) - min(abs(A[i-1]), abs(A[i]))
        else:
            ans += A[i-1]+A[i]

    if N % 2:
        ans += A[-1]

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
