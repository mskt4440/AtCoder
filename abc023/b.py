#
# abc023 b
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

    def test_入力例1(self):
        input = """3
abc"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
abcabc"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """7
atcoder"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """19
bcabcabcabcabcabcab"""
        output = """9"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = input()

    ans = 0
    s = "b"
    while len(s) < N:
        if ans % 3 == 0:
            s = "a" + s + "c"
        elif ans % 3 == 1:
            s = "c" + s + "a"
        elif ans % 3 == 2:
            s = "b" + s + "b"
        ans += 1
    if S != s:
        ans = -1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
