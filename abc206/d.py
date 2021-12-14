#
# abc206 d
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
        input = """8
1 5 3 2 5 2 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
1 2 3 4 1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
200000"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    L = [[]*N for _ in range(N)]
    for i in range(N//2):
        a, b = min(A[i], A[N-1-i]), max(A[i], A[N-1-i])
        if a != b:
            L[a].append(b)

    ans = 0
    for l in L:
        ans += len(l)
    print(ans)


if __name__ == "__main__":
    unittest.main()
    # resolve()
