#
# abc002 c
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
        input = """1 0 3 0 2 5"""
        output = """5.0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-1 -2 3 4 5 6"""
        output = """2.0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """298 520 903 520 4 663"""
        output = """43257.5"""
        self.assertIO(input, output)


def resolve():
    xa, ya, xb, yb, xc, yc = map(int, input().split())

    a = xb-xa
    b = yb-ya
    c = xc-xa
    d = yc-ya
    print(abs(a*d-b*c)/2)


if __name__ == "__main__":
    # unittest.main()
    resolve()
