#
# abc120 b
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

    def test_入力例_1(self):
        input = """8 12 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 50 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1 1"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    A, B, K = map(int, input().split())

    n = 0
    for i in range(min(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            n += 1
            if n == K:
                print(i)
                exit


if __name__ == "__main__":
    # unittest.main()
    resolve()
