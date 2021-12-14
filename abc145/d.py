#
# abc145 d
#
import sys
from io import StringIO
import unittest
from math import factorial


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
        input = """3 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999999 999999"""
        output = """151840682"""
        self.assertIO(input, output)


def resolve():
    X, Y = map(int, input().split())

    if (X+Y) % 3 or 2*Y-X < 0 or 2*X-Y < 0:
        print(0)
    else:
        n = (2*Y-X)//3
        m = (2*X-Y)//3
        print((factorial(n+m)//factorial(m)) % (10**9+7))


if __name__ == "__main__":
    unittest.main()
    # resolve()
