#
# abc138 a
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
        input = """3200
pink"""
        output = """pink"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3199
pink"""
        output = """red"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4049
red"""
        output = """red"""
        self.assertIO(input, output)


def resolve():
    a = int(input())
    s = input()

    if a >= 3200:
        print(s)
    else:
        print("red")


if __name__ == "__main__":
    # unittest.main()
    resolve()
