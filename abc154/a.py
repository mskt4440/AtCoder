#
# abc154 a
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
        input = """red blue
3 4
red"""
        output = """2 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """red blue
5 5
blue"""
        output = """5 4"""
        self.assertIO(input, output)


def resolve():
    S, T = map(str, input().split())
    A, B = map(int, input().split())
    U = input()

    if U == S:
        print(A-1, B)
    else:
        print(A, B-1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
