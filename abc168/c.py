#
# abc168 d
#
import sys
from io import StringIO
import unittest
import math


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
        input = """3 4 9 0"""
        output = """5.00000000000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 10 40"""
        output = """4.56425719433005567605"""
        self.assertIO(input, output)


def resolve():
    A, B, H, M = map(int, input().split())

    m = M/60
    h = H/12 + M/(60*12)
    d = abs(m-h)*2*math.pi

    print(math.sqrt(A**2+B**2-2*A*B*math.cos(d)))


if __name__ == "__main__":
    # unittest.main()
    resolve()
