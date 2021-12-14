#
# abc201 c
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
        input = """ooo???xxxx"""
        output = """108"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """o?oo?oxoxo"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """xxxxx?xxxo"""
        output = """15"""
        self.assertIO(input, output)


def resolve():
    S = input()


if __name__ == "__main__":
    unittest.main()
    # resolve()