#
# abc151 d
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
        input = """3 3
...
...
..."""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
...#.
.#.#.
.#..."""
        output = """10"""
        self.assertIO(input, output)


def resolve():
    global H, W
    H, W = map(int, input().split())
    global S
    S = [input() for _ in range(H)]

    ans = 0
    for sx in range(W):
        for sy in range(H):
            if S[sy][sx] == "#":
                continue
            ans = max(ans, route([sx, sy]))

    print(ans)


def route(s):
    f = True
    DX = [-1, 0, 1, 0]
    DY = [0, -1, 0, 1]
    F = [[-1]*W for _ in range(H)]
    q = deque()
    q.append(s)
    F[s[1]][s[0]] = 0
    while q:
        if not f:
            break
        px, py = q.popleft()
        ps = F[py][px]
        for dx, dy in zip(DX, DY):
            nx = px+dx
            ny = py+dy
            if nx < 0 or W <= nx or ny < 0 or H <= ny:
                continue
            if S[ny][nx] == "#" or F[ny][nx] != -1:
                continue
            F[ny][nx] = ps+1
            q.append([nx, ny])

    ret = -1
    for f in F:
        ret = max(ret, max(f))
    return ret


if __name__ == "__main__":
    # unittest.main()
    resolve()
