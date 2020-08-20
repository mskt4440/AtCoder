#
# abc072 c
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
        input = """7
3 1 4 1 5 9 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
0 1 2 3 4 5 6 7 8 9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
99999"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    AN = [0] * 100002  # -1 <= X <= 10^5+1

    for a in A:
        AN[a] += 1
        AN[a+1] += 1
        AN[a+2] += 1
    print(max(AN))


if __name__ == "__main__":
    # unittest.main()
    resolve()
