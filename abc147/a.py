#
# abc147 a
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
        input = """5 7 9"""
        output = """win"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """13 7 2"""
        output = """bust"""
        self.assertIO(input, output)


def resolve():
    a = list(map(int, input().split()))

    if sum(a) >= 22:
        print("bust")
    else:
        print("win")


if __name__ == "__main__":
    # unittest.main()
    resolve()
