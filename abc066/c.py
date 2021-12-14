#
# abc066 c
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
        input = """4
1 2 3 4"""
        output = """4 2 1 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 2 3"""
        output = """3 1 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
0 6 7 6 7 0"""
        output = """0 6 6 0 7 7"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(str, input().split()))

    ans = []
    for i in range(N-1, -1, -2):
        ans.append(A[i])
    if ans[-1] == A[0]:
        for i in range(1, N, 2):
            ans.append(A[i])
    else:
        for i in range(0, N, 2):
            ans.append(A[i])

    print(*ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
