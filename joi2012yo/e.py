#
# joi2012yo e
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
        input = """8 4
0 1 0 1 0 1 1 1
0 1 1 0 0 1 0 0
1 0 1 0 1 1 1 1
0 1 1 0 1 0 1 0"""
        output = """64"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 5
0 1 1 1 0 1 1 1
0 1 0 0 1 1 0 0
1 0 0 1 1 1 1 1
0 1 0 1 1 0 1 0
0 1 1 0 1 1 0 0"""
        output = """56"""
        self.assertIO(input, output)


def resolve():
    W, H = map(int, input().split())
    M = [[0]*(W+2)]
    for _ in range(H):
        M.append([0] + list(map(int, input().split())) + [0])
    M.append([0]*(W+2))

    D = [[False]*(W+2) for _ in range(H+2)]
    Q = deque()

    dy = [0, 0, 1, 1, -1, -1]
    dox = [-1, 1, 0, 1, 0, 1]
    dex = [-1, 1, -1, 0, -1, 0]

    Q.append([0, 0])
    D[0][0] = True

    ans = 0
    while Q:
        p = Q.popleft()
        x, y = p

        for i in range(6):
            ny = y + dy[i]
            nx = x
            if y % 2:
                nx += dox[i]
            else:
                nx += dex[i]

            if nx < 0 or nx > W+1 or ny < 0 or ny > H+1 or D[ny][nx]:
                continue

            if M[ny][nx] == 1:
                ans += 1
            else:
                Q.append([nx, ny])
                D[ny][nx] = True

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
