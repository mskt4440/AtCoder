#
# abc049 a
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
        input = """a"""
        output = """vowel"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """z"""
        output = """consonant"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """s"""
        output = """consonant"""
        self.assertIO(input, output)


def resolve():
    c = input()
    if c == "a" or c == "i" or c == "u" or c == "e" or c == "o":
        print("vowel")
    else:
        print("consonant")


if __name__ == "__main__":
    # unittest.main()
    resolve()
