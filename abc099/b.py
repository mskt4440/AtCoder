#
# abc099 b
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
        input = """8 13"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """54 65"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    print(sum(range(B-A))-A)


if __name__ == "__main__":
    # unittest.main()
    resolve()
