#
# abc059 a
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
        input = """atcoder beginner contest"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """resident register number"""
        output = """RRN"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """k nearest neighbor"""
        output = """KNN"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """async layered coding"""
        output = """ALC"""
        self.assertIO(input, output)


def resolve():
    s = list(input().split())
    ans = s[0][0]+s[1][0]+s[2][0]
    print(ans.upper())


if __name__ == "__main__":
    # unittest.main()
    resolve()
