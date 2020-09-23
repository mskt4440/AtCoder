#
# abc128 c
#

import sys
from io import StringIO
import unittest
from collections import deque


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
        input = """2 2
2 1 2
1 2
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
2 1 2
1 1
1 2
0 0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2
3 1 2 5
2 2 3
1 0"""
        output = """8"""
        self.assertIO(input, output)


def resolve_bit():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))

    ans = 0
    for bit in range(1 << N):
        m = 0
        for i in range(M):
            t = 0
            for j in range(1, S[i][0]+1):
                if bit & (1 << (S[i][j]-1)):
                    t += 1
            if t % 2 != P[i]:
                break
            else:
                m += 1
        if m == M:
            ans += 1
    print(ans)


def resolve():
    global N, M, KS, P
    N, M = map(int, input().split())
    KS = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))

    ONS = deque()
    print(dfs(0, ONS))


def dfs(n, T):
    if n == N:
        onm = 0
        for i, ks in enumerate(KS):
            k, s = ks[0], ks[1:]
            onsn = 0
            for t in T:
                if t in s:
                    onsn += 1
            if onsn % 2 != P[i]:
                break
            else:
                onm += 1
        if onm == M:
            return 1
        else:
            return 0

    ans = 0
    T.append(n+1)
    ans += dfs(n+1, T)
    T.pop()
    ans += dfs(n+1, T)
    return ans


if __name__ == "__main__":
    # unittest.main()
    resolve()
