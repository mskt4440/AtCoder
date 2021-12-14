#
# abc122 a
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
        input = """A"""
        output = """T"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """G"""
        output = """C"""
        self.assertIO(input, output)


def resolve():
    b = input()

    if b == "A":
        print("T")
    elif b == "T":
        print("A")
    elif b == "C":
        print("G")
    elif b == "G":
        print("C")


if __name__ == "__main__":
    # unittest.main()
    resolve()
