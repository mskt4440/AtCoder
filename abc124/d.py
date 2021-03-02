#
# abc124 d
#
import sys
from io import StringIO
import unittest
import itertools


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
        input = """5 1
00010"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14 2
11101010110011"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1
1"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    S = input()

    c = S[0]
    n = 1
    L = []
    if S[0] == "0":
        L.append(0)
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            n += 1
        else:
            L.append(n)
            n = 1
    else:
        L.append(n)
    if S[-1] == "0":
        L.append(0)

    A = [0]
    for l in L:
        A.append(A[-1]+l)
    ans = 0
    for l in range(1, len(A), 2):
        r = min(l+2*K*1, len(A)-1)
        ans = max(ans, A[r] - A[l-1])
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
