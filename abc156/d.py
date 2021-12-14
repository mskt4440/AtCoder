#
# abc156 d
#
import sys
from io import StringIO
import unittest
from math import factorial


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
        input = """4 1 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 141421 173205"""
        output = """34076506"""
        self.assertIO(input, output)


def resolve():
    N, A, B = map(int, input().split())

    MOD = 10**9+7
    (1 << N)-1 - factorial()


if __name__ == "__main__":
    unittest.main()
    # resolve()
