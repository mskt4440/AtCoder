#
# abc013 b
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
        input = """4
6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """8
1"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    a = int(input())
    b = int(input())
    t = abs(a-b)
    print(min(t, 10-t))


if __name__ == "__main__":
    # unittest.main()
    resolve()
