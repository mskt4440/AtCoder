#
# abc187 c
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

    def test_入力例_1(self):
        input = """6
a
!a
b
!c
d
!d"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
red
red
red
!orange
yellow
!blue
cyan
!green
brown
!gray"""
        output = """satisfiable"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = [input() for _ in range(N)]

    ans = "satisfiable"

    SS = set(S)
    for s in S:
        if "!"+s in SS:
            print(s)
            break
    else:
        print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
