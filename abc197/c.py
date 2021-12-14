#
# abc197 c
#
from abc import abstractclassmethod
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
        input = """3
1 5 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
10 10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 3 3 1"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    for bit in range(1 << N-1):
        T = []
        for j in range(N):


if __name__ == "__main__":
    # unittest.main()
    resolve()
