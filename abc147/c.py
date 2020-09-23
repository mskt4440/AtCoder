#
# abc147 c
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
        input = """3
1
2 1
1
1 1
1
2 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1
2 0
1
1 0"""
        output = """1"""
        self.assertIO(input, output)


def resolve_bit():
    N = int(input())
    C = []
    for i in range(N):
        a = int(input())
        C.append([list(map(int, input().split())) for j in range(a)])

    ans = 0
    for bit in range(1 << N):
        f = True
        for i in range(N):
            if bit & (1 << i):
                for c in C[i]:
                    if bit & (1 << c[0]-1) != (1 << c[0]-1)*c[1]:
                        f = False
                        break
        if f == True:
            ans = max(ans, bin(bit).count("1"))
    print(ans)


def resolve():
    global N, C
    N = int(input())
    C = []
    for i in range(N):
        a = int(input())
        C.append([list(map(int, input().split())) for j in range(a)])

    V = deque()
    print(dfs(0, V))


def dfs(n, V):
    if n == N:
        count = 0
        for v in V:
            if count == -1:
                break
            for c in C[v-1]:
                if (c[0] in V and c[1] == 0) or (c[0] not in V and c[1] == 1):
                    count = -1
                    break
            else:
                count += 1
        if count == -1:
            return 0
        else:
            return count

    ans = 0
    V.append(n+1)
    ans = max(ans, dfs(n+1, V))
    V.pop()
    ans = max(ans, dfs(n+1, V))

    return ans


if __name__ == "__main__":
    # unittest.main()
    resolve()
