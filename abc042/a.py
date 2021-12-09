#
# abc042 a
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
        input = """5 5 7"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 7 5"""
        output = """NO"""
        self.assertIO(input, output)


def resolve():
    L = list(input().split())
    if L.count("5") == 2 and L.count("7") == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # unittest.main()
    resolve()
