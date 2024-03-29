#
# abc076 a
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
        input = """2002
2017"""
        output = """2032"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4500
0"""
        output = """-4500"""
        self.assertIO(input, output)


def resolve():
    R = int(input())
    G = int(input())

    print(2*G-R)


if __name__ == "__main__":
    # unittest.main()
    resolve()
