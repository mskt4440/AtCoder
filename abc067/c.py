#
# abc067 c
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
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
10 -10"""
        output = """20"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = float("inf")
    S = sum(A)
    T = []
    T.append(A[0])
    for i in range(1, N-1):
        T.append(T[i-1]+A[i])
    for t in T:
        ans = min(ans, abs(S-2*t))

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
