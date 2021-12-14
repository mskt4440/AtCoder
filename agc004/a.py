#
# agc004 a
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
        input = """3 3 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 3 5"""
        output = """15"""
        self.assertIO(input, output)


def resolve():
    ABC = list(map(int, input().split()))
    ABC.sort()
    AB = ABC[0]*ABC[1]

    if ABC[2] % 2:
        print(AB)
    else:
        print("0")


if __name__ == "__main__":
    # unittest.main()
    resolve()
