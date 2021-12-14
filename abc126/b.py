#
# abc126 b
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
        input = """1905"""
        output = """YYMM"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0112"""
        output = """AMBIGUOUS"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1700"""
        output = """NA"""
        self.assertIO(input, output)


def resolve():
    S = input()

    if 1 <= int(S[:2]) <= 12 and 1 <= int(S[2:]) <= 12:
        print("AMBIGUOUS")
    elif 1 <= int(S[:2]) <= 12:
        print("MMYY")
    elif 1 <= int(S[2:]) <= 12:
        print("YYMM")
    else:
        print("NA")


if __name__ == "__main__":
    # unittest.main()
    resolve()
