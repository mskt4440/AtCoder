#
# abcw196 a
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
        input = """0 10
0 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-100 -100
100 100"""
        output = """-200"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """-100 100
-100 100"""
        output = """200"""
        self.assertIO(input, output)


def resolve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    print(b-c)


if __name__ == "__main__":
    # unittest.main()
    resolve()
