#
# abc063 b
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
        input = """uncopyrightable"""
        output = """yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """different"""
        output = """no"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """no"""
        output = """yes"""
        self.assertIO(input, output)


def resolve():
    S = list(input())
    SS = set(S)

    if len(S) == len(SS):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    # unittest.main()
    resolve()
