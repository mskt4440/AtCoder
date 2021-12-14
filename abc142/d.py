#
# abc142 d
#
from math import factorial
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
        input = """12 18"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """420 660"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2019"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    m = math.gcd(A, B)
    if m == 1:
        print("1")
    else:
        f = factorization(m)
        print(len(f)+1)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


if __name__ == "__main__":
    # unittest.main()
    resolve()
