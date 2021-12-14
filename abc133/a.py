#
# abc133 a
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
        input = """4 2 9"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2 7"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 2 8"""
        output = """8"""
        self.assertIO(input, output)


def resolve():
    N, A, B = map(int, input().split())

    print(min(N*A, B))


if __name__ == "__main__":
    # unittest.main()
    resolve()
