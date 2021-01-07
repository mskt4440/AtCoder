#
# abc064 d
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
        input = """3
())"""
        output = """(())"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
)))())"""
        output = """(((()))())"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
))))(((("""
        output = """(((())))(((())))"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = input()

    l = 0
    r = 0

    for s in S:
        if s == "(":
            l += 1
        else:
            if l > 0:
                l -= 1
            else:
                r += 1
    ans = "("*r + S + ")"*l
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
