#
# cpscoO2019s1
#
import sys
from io import StringIO
import unittest
sys.setrecursionlimit(10 ** 6)


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
        input = """3 2
25 29 62"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
10000 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 3
1415 9265 3589 7932 3846 2643 3832 7950 2884 1971"""
        output = """5"""
        self.assertIO(input, output)


def resolve():
    global K
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    print(dfs(A, 0, 0, float("inf")))


def dfs(L, n, s, ans):
    if n == K:
        ss = str(s)
        nc = 0
        for i in range(len(ss)):
            x = int(ss[i])
            if x >= 5:
                nc += x-4
            else:
                nc += x
        return nc

    for i, l in enumerate(L):
        ans = min(ans, dfs(L[i+1:], n+1, s+l, ans))
    return ans


if __name__ == "__main__":
    # unittest.main()
    resolve()
