#
# abcw197 a
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
        input = """abc"""
        output = """bca"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aab"""
        output = """aba"""
        self.assertIO(input, output)


def resolve():
    S = input()
    print(S[1:]+S[0])


if __name__ == "__main__":
    # unittest.main()
    resolve()
