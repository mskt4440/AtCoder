#
# abc037 c
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
        input = """5 3
1 2 4 8 16"""
        output = """49"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 10
100000000 100000000 98667799 100000000 100000000 100000000 100000000 99986657 100000000 100000000 100000000 100000000 100000000 98995577 100000000 100000000 99999876 100000000 100000000 99999999"""
        output = """10988865195"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    S = [0]*N
    for i, a in enumerate(A):
        if i == 0:
            S[i] = a
        else:
            S[i] = S[i-1] + a

    ans = 0
    for i in range(N):
        if i == 0:
            ans += S[K-1]
        elif i+K <= N:
            ans += S[i+K-1]-S[i-1]
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
