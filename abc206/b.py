#
# abc206 b
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
        input = """12"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100128"""
        output = """447"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    s = 0
    for i in range(1, N+1):
        s += i
        if s >= N:
            print(i)
            break


if __name__ == "__main__":
    # unittest.main()
    resolve()
