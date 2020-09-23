#
# abc165 c
#
import sys
from io import StringIO
import unittest
sys.setrecursionlimit(100000)


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
        input = """3 4 3
1 3 3 100
1 2 2 10
2 3 2 10"""
        output = """110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 6 10
2 4 1 86568
1 4 0 90629
2 3 0 90310
3 4 1 29211
3 4 3 78537
3 4 2 8580
1 2 1 96263
1 4 2 2156
1 2 0 94325
1 4 3 94328"""
        output = """357500"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 1
1 10 9 1"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    global N, M, ABCD
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]

    print(dfs([1]))


def dfs(L):
    if len(L) == N:
        score = 0
        for abcd in ABCD:
            a, b, c, d = abcd
            if L[b-1] - L[a-1] == c:
                score += d
        return score

    ans = 0
    for i in range(L[-1], M+1):
        NL = L + [i]
        ans = max(ans, dfs(NL))

    return ans


if __name__ == "__main__":
    # unittest.main()
    resolve()
