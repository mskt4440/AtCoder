#
# abc176 c
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
2 1 5 4 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
3 3 3 3 3"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    M = A[0]
    ans = 0
    for i in range(1, N):
        if A[i] < M:
            ans += M-A[i]
        else:
            M = A[i]
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
