#
# abc110 a
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
        input = """1 5 2"""
        output = """53"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 9 9"""
        output = """108"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 6 7"""
        output = """82"""
        self.assertIO(input, output)


def resolve():
    L = list(map(int, input().split()))
    L.sort()
    print(L[-1]*10+L[0]+L[1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
