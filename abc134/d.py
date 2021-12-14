#
# abc134 d
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
1 0 0"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    B = [-1]*N
    for i in range(N, 0, -1):
        t = 0
        for j in range(i*2, N+1, i):
            t += B[j-1]
        if t % 2 == A[i-1]:
            B[i-1] = 0
        else:
            B[i-1] = 1

    s = sum(B)
    print(s)
    if s:
        ans = []
        for i, b in enumerate(B, 1):
            if b:
                ans.append(i)
        print(*ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
