#
# abc031 c
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

    def test_入力例1(self):
        input = """6
1 -3 3 9 1 6"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3
5 5 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """8
-1 10 -1 2 -1 10 -1 0"""
        output = """-1"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = -50*N
    for i in range(N):
        tsc = [-50*N] * N
        asc = [-50*N] * N
        for j in range(N):
            if i == j:
                continue

            T = A[min(i, j):max(i, j)+1]

            tsc[j] = sum(T[::2])
            asc[j] = sum(T[1::2])
        ai = asc.index(max(asc))
        ans = max(ans, tsc[ai])

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
