#
# abc188 e
#
import collections
import sys
from io import StringIO
import unittest
from collections import deque


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
        input = """4 3
2 3 1 5
2 4
1 2
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
13 8 3 15 18
2 4
1 2
4 5
2 3
1 3"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1
1 100 1
2 3"""
        output = """-99"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]


if __name__ == "__main__":
    unittest.main()
    # resolve()
