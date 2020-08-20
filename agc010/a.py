#
# agc010 a
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
1 2 3"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2 3 4 5"""
        output = """NO"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    if sum(A) % 2 == 0:
        print("YES")
    else:
        print("NO")
#    e = 0
#    o = 0
#    for a in A:
#        if a % 2 == 0:
#            e += 1
#        else:
#            o += 1
#
#    if o % 2 == 0:
#        print("YES")
#    else:
#        print("NO")


if __name__ == "__main__":
    unittest.main()
    # resolve()
