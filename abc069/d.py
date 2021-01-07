#
# abc069 d
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
3
2 1 1"""
        output = """1 1
2 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
5
1 2 3 4 5"""
        output = """1 4 4 4 3
2 5 4 5 3
2 5 5 5 3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1
1
1"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    N = int(input())
    A = list(map(int, input().split()))

    ans = [[0] * W for _ in range(H)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    p = [0, 0]
    ci = 0
    cn = A[0]-1
    ans[0][0] = ci+1
    q = deque()
    q.append(p)

    while q:
        x, y = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or W <= nx or ny < 0 or H <= ny or ans[ny][nx]:
                continue

            if cn == 0:
                ci += 1
                cn = A[ci]
            ans[ny][nx] = ci+1
            cn -= 1
            q.append([nx, ny])
            break

    for l in ans:
        print(*l)


if __name__ == "__main__":
    # unittest.main()
    resolve()
