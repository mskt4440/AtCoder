#
# abc015 c
#
import sys
from io import StringIO
from typing import AnyStr
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

    def test_入力例1(self):
        input = """3 4
1 3 5 17
2 4 2 3
1 3 2 9"""
        output = """Found"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 3
89 62 15
44 36 17
4 24 24
25 98 99
66 33 57"""
        output = """Nothing"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    q = deque()
    q.append([0, 0])
    ans = "Nothing"

    while q:
        p = q.pop()
        n = p[0]
        v = p[1]

        if n == N:
            if v == 0:
                ans = "Found"
                break
            else:
                continue

        for t in T[n]:
            q.append([n+1, v ^ t])

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
