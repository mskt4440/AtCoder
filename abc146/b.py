#
# abc146 b
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
        input = """2
ABCXYZ"""
        output = """CDEZAB"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0
ABCXYZ"""
        output = """ABCXYZ"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """13
ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
        output = """NOPQRSTUVWXYZABCDEFGHIJKLM"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = input()

    ans = ""
    for s in S:
        t = ord(s)+N
        if t > ord("Z"):
            t = t - ord("Z") + ord("A") - 1
        ans += chr(t)

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
