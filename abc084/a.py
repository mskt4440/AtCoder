#
# abc084 a
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
        input = """21"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12"""
        output = """36"""
        self.assertIO(input, output)


def resolve():
    M = int(input())
    print(48-M)


if __name__ == "__main__":
    # unittest.main()
    resolve()
