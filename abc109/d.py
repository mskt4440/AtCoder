#
# abc109 d
#
import sys
from io import StringIO
import unittest


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
        input = """2 3
1 2 3
0 1 1"""
        output = """3
2 2 2 3
1 1 1 2
1 3 1 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
1 0
2 1
1 0"""
        output = """3
1 1 1 2
1 2 2 2
3 1 3 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 5
9 9 9 9 9"""
        output = """2
1 1 1 2
1 3 1 4"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    L = []
    for h in range(H):
        if h % 2 == 0:
            for w in range(W):
                L.append([h, w])
        else:
            for w in reversed(range(W)):
                L.append([h, w])

    ans = []
    for i in range(H*W-1):
        if A[L[i][0]][L[i][1]] % 2:
            A[L[i][0]][L[i][1]] -= 1
            A[L[i+1][0]][L[i+1][1]] += 1
            ans.append([L[i][0]+1, L[i][1]+1, L[i+1][0]+1, L[i+1][1]+1])

    print(len(ans))
    for a in ans:
        print(*a)


if __name__ == "__main__":
    # unittest.main()
    resolve()
