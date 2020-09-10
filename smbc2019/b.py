#
# smbc2019 b
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
        input = """432"""
        output = """400"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1079"""
        output = """:("""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1001"""
        output = """927"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    for x in range(1, N+1):
        if math.floor(x*1.08) == N:
            print(x)
            break
    else:
        print(":(")


if __name__ == "__main__":
    # unittest.main()
    resolve()
