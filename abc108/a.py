#
# abc108 a
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
        input = """3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """50"""
        output = """625"""
        self.assertIO(input, output)


def resolve():
    K = int(input())

    x = K//2
    print(x*(K-x))


if __name__ == "__main__":
    # unittest.main()
    resolve()
