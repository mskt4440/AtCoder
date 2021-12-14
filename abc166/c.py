#
# abc166 c
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
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    G = [[i] for i in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    ans = 0
    for g in G:
        if len(g) == 1:
            ans += 1
            continue
        for n in g[1:]:
            if H[n] >= H[g[0]]:
                break
        else:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
