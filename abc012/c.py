#
# abc012 c
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

    def test_入力例1(self):
        input = """2013"""
        output = """2 x 6
3 x 4
4 x 3
6 x 2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2024"""
        output = """1 x 1"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    s = 0
    for i in range(1, 10):
        for j in range(1, 10):
            s += i*j

    t = s-N
    for i in range(1, 10):
        for j in range(1, 10):
            if i*j == t:
                print(f"{i} x {j}")


if __name__ == "__main__":
    # unittest.main()
    resolve()
