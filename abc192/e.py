#
# abc192 e
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
        input = """3 2 1 3
1 2 2 3
2 3 3 4"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2 3 1
1 2 2 3
2 3 3 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 0 3 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """9 14 6 7
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3
2 3 8 4
6 2 6 4
3 8 3 2
7 9 5 2
8 4 1 9
7 1 6 9
3 9 9 3
7 5 1 5
8 2 9 7
4 9 4 4"""
        output = """26"""
        self.assertIO(input, output)


def resolve():
    N, M, X, Y = map(int, input())


if __name__ == "__main__":
    unittest.main()
    # resolve()
