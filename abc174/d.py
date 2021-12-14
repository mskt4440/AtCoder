#
# abc174 d
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
        input = """4
WWRR"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
RR"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
WRWWRWRR"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    C = input()

    r = C.count("R")
    print(C[:r].count("W"))


if __name__ == "__main__":
    # unittest.main()
    resolve()
