#
# abc107 c
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
-30 -10 10 20 50"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
10 20 30"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1
0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8 5
-9 -7 -4 -3 1 2 3 4"""
        output = """10"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))

    if 0 in set(X):
        X.remove(0)
        K -= 1
    if K == 0:
        print(0)
    else:
        D = [0]
        for i in range(1, N):
            D.append(D[-1]+abs(X[i]-X[i-1]))

        ans = float("inf")
        for i in range(N-K+1):
            p = min(abs(X[i]), abs(X[i+K-1]))
            ans = min(ans, p+D[K+i-1]-D[i])

        print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
