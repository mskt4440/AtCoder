#
# abc014 a
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
        input = """7
3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1
100"""
        output = """99"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """25
12"""
        output = """11"""
        self.assertIO(input, output)


def resolve():
    a = int(input())
    b = int(input())

    if a % b:
        print(b-a % b)
    else:
        print("0")


if __name__ == "__main__":
    # unittest.main()
    resolve()
