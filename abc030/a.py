#
# abc030 a
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
        input = """5 2 6 3"""
        output = """AOKI"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """100 80 100 73"""
        output = """TAKAHASHI"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """66 30 55 25"""
        output = """DRAW"""
        self.assertIO(input, output)


def resolve():
    A, B, C, D = map(int, input().split())

    t = B/A
    a = D/C
    if t > a:
        print("TAKAHASHI")
    elif t < a:
        print("AOKI")
    else:
        print("DRAW")


if __name__ == "__main__":
    # unittest.main()
    resolve()
