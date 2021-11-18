#
# abc023 d
#
import sys
from io import StringIO
import unittest
import bisect


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
        input = """4
5 6
12 4
14 7
21 2"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
100 1
100 1
100 1
100 1
100 1
1 30"""
        output = """105"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    ok = 0
    global H, S
    H = []
    S = []
    for _ in range(N):
        h, s = map(int, input().split())
        H.append(h)
        S.append(s)
        ok = max(ok, h+s*(N-1))

    ok -= 1
    ng = max(H)-1

    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if isOK(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


def isOK(x):
    time = [(x-h)/s for (h, s) in zip(H, S)]
    time.sort()
    for i, t in enumerate(time):
        if i > t:
            return False
    return True


if __name__ == "__main__":
    # unittest.main()
    resolve()
