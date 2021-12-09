#
# abc033 a
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
        input = """2222"""
        output = """SAME"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1221"""
        output = """DIFFERENT"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0000"""
        output = """SAME"""
        self.assertIO(input, output)


def resolve():
    N = list(input())
    if N.count(N[0]) == 4:
        print("SAME")
    else:
        print("DIFFERENT")


if __name__ == "__main__":
    # unittest.main()
    resolve()
