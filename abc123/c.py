#
# abc123 c
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
        input = """5
3
2
4
3
5"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
123
123
123
123
123"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000007
2
3
5
7
11"""
        output = """5000000008"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    L = (a, b, c, d, e)

    print((N+min(L)-1)//min(L) + 4)


if __name__ == "__main__":
    # unittest.main()
    resolve()
