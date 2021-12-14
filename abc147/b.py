#
# abc147 b
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
        input = """redcoder"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """vvvvvv"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcdabc"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    S = input()

    n = len(S)
    ans = 0
    for i in range(n//2):
        if S[i] != S[n-1-i]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
