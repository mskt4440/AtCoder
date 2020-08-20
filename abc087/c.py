#
# abc087 c
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
3 2 2 4 1
1 2 2 2 1"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1
1 1 1 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
3 3 4 5 4 5 3
5 3 4 4 2 3 2"""
        output = """29"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
2
3"""
        output = """5"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]

    ans = 0
    if N == 1:
        ans = A[0][0]+A[1][0]
    else:
        #        for i in range(N):
        #            ans = max(ans, sum(A[0])+A[1][N-1],
        #                      sum(A[0][:N-1-i])+sum(A[1][N-1-i-1:]))

        for i in range(N):
            ans = max(ans, sum(A[0])+A[1][-1],
                      sum(A[0][:-2-i+1])+sum(A[1][-2-i:]))

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
