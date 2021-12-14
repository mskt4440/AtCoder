#
# abc100 a
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
        input = """5 4"""
        output = """Yay!"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 8"""
        output = """Yay!"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 4"""
        output = """:("""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    if A <= 8 and B <= 8:
        print("Yay!")
    else:
        print(":(")


if __name__ == "__main__":
    # unittest.main()
    resolve()
