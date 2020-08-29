#
# abc177 b
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
        input = """cabacc
abc"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """codeforces
atcoder"""
        output = """6"""
        self.assertIO(input, output)


def resolve():
    S = input()
    T = input()

    ans = float("inf")
    for i in range(len(S)-len(T)+1):
        tmp = 0
        for j in range(len(T)):
            if T[j] != S[i+j]:
                tmp += 1
        ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
