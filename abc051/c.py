#
# abc051 c
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
        input = """0 0 1 2"""
        output = """UURDDLLUUURRDRDDDLLU"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-2 -2 1 1"""
        output = """UURRURRDDDLLDLLULUUURRURRDDDLLDL"""
        self.assertIO(input, output)


def resolve():
    sx, sy, tx, ty = map(int, input().split())

    ans = "U"*(ty-sy) + "R"*(tx-sx)
    ans += "D"*(ty-sy) + "L"*(tx-sx)
    ans += "L" + "U"*(ty-sy+1) + "R"*(tx-sx+1) + "D"
    ans += "R" + "D"*(ty-sy+1) + "L"*(tx-sx+1) + "U"

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
