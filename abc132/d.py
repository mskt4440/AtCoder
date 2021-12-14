#
# abc132 d
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
        input = """5 3"""
        output = """3
6
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2000 3"""
        output = """1998
3990006
327341989"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())

    for i in range(K):
        if N-K+1 >= i+1:
            r = math.factorial(N-K+1)//(math.factorial(N-K-i)
                                        * math.factorial(i+1))
            b = math.factorial(K-1)//(math.factorial(K-1-i)*math.factorial(i))
            print((r*b) % (10**9+7))
        else:
            print(0)


if __name__ == "__main__":
    # unittest.main()
    resolve()
