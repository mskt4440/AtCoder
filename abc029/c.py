#
# abc029 c
#
import sys
from io import StringIO
import unittest
from itertools import product


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
        input = """1"""
        output = """a
b
c"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2"""
        output = """aa
ab
ac
ba
bb
bc
ca
cb
cc"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    P = product("abc", repeat=N)

    for p in P:
        for v in p:
            print(v, end="")
        print()


if __name__ == "__main__":
    # unittest.main()
    resolve()
