#
# abc162 d
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
        input = """4
RRGB"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB"""
        output = """1800"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = input()

    R = []
    B = []
    G = []
    for i, s in enumerate(S):
        if s == "R":
            R.append(i)
        if s == "G":
            G.append(i)
        if s == "B":
            B.append(i)

    ans = len(R)*len(G)*len(B)

    for i in range(N):
        for j in range(1, N):
            if i+j > N-1:
                break
            if i+2*j > N-1:
                break
            if S[i] != S[i+j] and S[i+j] != S[i+j*2] and S[i+j*2] != S[i]:
                ans -= 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
