#
# abc208 e
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
        input = """13 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 80"""
        output = """99"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000 1000000000"""
        output = """841103275147365677"""
        self.assertIO(input, output)


def resolve():


if __name__ == "__main__":
    unittest.main()
    # resolve()
