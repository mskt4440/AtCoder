#
# abc004 b
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
        input = """. . . .
. o o .
. x x .
. . . ."""
        output = """. . . .
. x x .
. o o .
. . . ."""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """o o x x
o o x x
x x o o
x x o o"""
        output = """o o x x
o o x x
x x o o
x x o o"""
        self.assertIO(input, output)


def resolve():
    C = [list(input().split()) for _ in range(4)]

    ans = [["_"]*4 for _ in range(4)]
    for i, c in enumerate(C):
        if i == 0:
            ans[3] = reversed(c)
        elif i == 1:
            ans[2] = reversed(c)
        elif i == 2:
            ans[1] = reversed(c)
        else:
            ans[0] = reversed(c)

    for a in ans:
        print(*a)


if __name__ == "__main__":
    # unittest.main()
    resolve()
