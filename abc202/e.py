#
# abc202 e
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
        input = """2 2 4"""
        output = """baab"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """30 30 118264581564861424"""
        output = """bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        self.assertIO(input, output)


def resolve():
    A, B, K = map(int, input().split())


if __name__ == "__main__":
    unittest.main()
    # resolve()
