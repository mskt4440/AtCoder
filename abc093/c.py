#
# abc093 c
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
        input = """2 5 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 6 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31 41 5"""
        output = """23"""
        self.assertIO(input, output)


def resolve():
    I = list(map(int, input().split()))
    I.sort()

    t = 2*I[2]-I[0]-I[1]
    # X = max(A, B, C)
    if t % 2 == 0:
        print(t//2)
    # X = max(A, B, C) + 1
    else:
        print((t+3)//2)


if __name__ == "__main__":
    # unittest.main()
    resolve()
