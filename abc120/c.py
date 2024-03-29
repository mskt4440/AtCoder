#
# abc120 c
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
        input = """0011"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11011010001011"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    S = input()

    print(min(S.count("0"), S.count("1"))*2)


if __name__ == "__main__":
    # unittest.main()
    resolve()
