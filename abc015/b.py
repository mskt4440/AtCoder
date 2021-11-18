#
# abc015 b
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

    def test_入力例1(self):
        input = """4
0 1 3 8"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
1 4 9 10 15"""
        output = """8"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    t = 0
    n = 0
    for a in A:
        if a == 0:
            continue
        t += a
        n += 1

    print(math.ceil(t/n))


if __name__ == "__main__":
    # unittest.main()
    resolve()
