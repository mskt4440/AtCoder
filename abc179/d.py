#
# abc170 d
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
        input = """5 2
1 1
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
3 3
5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1
1 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """60 3
5 8
1 3
10 15"""
        output = """221823067"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]

    S = []
    for lr in LR:
        l, r = lr
        S += range(l, r+1)

    ANS = [0] * N
    Q = deque()
    ANS[0] += 1
    Q.append(1)

    while Q:
        p = Q.popleft()

        if p == N:
            continue

        for dp in S:
            np = p + dp
            if np > N:
                continue

            ANS[np-1] += 1
            Q.append(np)

    print(ANS[-1] % 998244353)


if __name__ == "__main__":
    unittest.main()
    # resolve()
