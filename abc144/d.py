#
# abc144 d
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
        input = """2 2 4"""
        output = """45.0000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12 21 10"""
        output = """89.7834636934"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1 8"""
        output = """4.2363947991"""
        self.assertIO(input, output)


def resolve():
    a, b, x = map(int, input().split())

    if a*a*b/2 < x:
        print(math.degrees(math.atan(2*(b/a-x/(a**3)))))
    else:
        print(math.degrees(math.pi/2 - math.atan(2*x/(a*b*b))))


if __name__ == "__main__":
    # unittest.main()
    resolve()
