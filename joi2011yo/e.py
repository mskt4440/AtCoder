#
# joi2011yo e
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
        input = """3 3 1
S..
...
..1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5 2
.X..1
....X
.XX.S
.2.X."""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 9
.X...X.S.X
6..5X..X1X
...XXXX..X
X..9X...X.
8.X2X..X3X
...XX.X4..
XX....7X..
X..X..XX..
X...X.XX..
..X......."""
        output = """91"""
        self.assertIO(input, output)


def resolve():
    H, W, N = map(int, input().split())
    Map = [list(input()) for _ in range(H)]

    SGX = [-1] * (N+1)
    SGY = [-1] * (N+1)
    SG = ["S"]
    for sg in range(1, N+1):
        SG.append(str(sg))

    for r, l in enumerate(Map):
        for sg in SG:
            if sg in l:
                if sg == "S":
                    SGX[0] = l.index(sg)
                    SGY[0] = r
                else:
                    sgi = int(sg)
                    SGX[sgi] = l.index(sg)
                    SGY[sgi] = r

    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    ans = 0
    for i in range(N):
        Q = deque()
        D = [[-1]*W for _ in range(H)]

        Q.append([SGX[i], SGY[i]])
        D[SGY[i]][SGX[i]] = 0

        while Q:
            p = Q.popleft()
            x, y = p

            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if nx == SGX[i+1] and ny == SGY[i+1]:
                    ans += D[y][x] + 1
                    Q.clear()
                    break

                if nx < 0 or nx >= W or ny < 0 or ny >= H or Map[ny][nx] == "X" or D[ny][nx] != -1:
                    continue
                Q.append([nx, ny])
                D[ny][nx] = D[y][x] + 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
