#
# abc023 a
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
        input = """23"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """70"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """99"""
        output = """18"""
        self.assertIO(input, output)


def resolve():
    X = input()
    print(int(X[0])+int(X[1]))


if __name__ == "__main__":
    # unittest.main()
    resolve()
