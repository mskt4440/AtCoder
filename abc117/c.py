#
# abc117 c
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
        input = """2 5
10 12 1 2 14"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 7
-10 -3 0 9 -100 2 17"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 1
-100000"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))

    if N >= M:
        print(0)
    else:
        X.sort()
        D = []
        for i in range(M-1):
            D.append(X[i+1]-X[i])
        D.sort()
        for i in range(N-1):
            D.pop()
        print(sum(D))


if __name__ == "__main__":
    # unittest.main()
    resolve()
