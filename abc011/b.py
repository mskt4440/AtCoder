#
# abc011 b
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

    def test_入力例1(self):
        input = """taKahAshI"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """A"""
        output = """A"""
        self.assertIO(input, output)


def resolve():
    S = input()
    if len(S) == 1:
        print(S.upper())
    else:
        print(S[0].upper()+S[1:].lower())


if __name__ == "__main__":
    # unittest.main()
    resolve()
