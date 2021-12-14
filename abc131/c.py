#
# abc131 c
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
        input = """4 9 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 40 6 8"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265358979323 846264338327950288 419716939 937510582"""
        output = """532105071133627368"""
        self.assertIO(input, output)


def resolve():
    A, B, C, D = map(int, input().split())

    cn = B//C - (A-1)//C
    dn = B//D - (A-1)//D
    cd = C*D//math.gcd(C, D)
    cdn = B//cd - (A-1)//cd

    print(B-A+1-cn-dn+cdn)


if __name__ == "__main__":
    # unittest.main()
    resolve()
