#
# abc148 a
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
        input = """3
1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
2"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    A = int(input())
    B = int(input())

    print(6-A-B)


if __name__ == "__main__":
    # unittest.main()
    resolve()
