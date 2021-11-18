#
# abc025 a
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
        input = """abcde
8"""
        output = """bc"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """aeiou
22"""
        output = """ue"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """vwxyz
25"""
        output = """zz"""
        self.assertIO(input, output)


def resolve():
    S = input()
    N = int(input())

    i = (N-1)//5
    j = (N-1) % 5
    print(S[i]+S[j])


if __name__ == "__main__":
    # unittest.main()
    resolve()
