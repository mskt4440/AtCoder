#
# abc159 d
#
import sys
from io import StringIO
import unittest
from collections import Counter


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
        input = """5
1 1 2 1 2"""
        output = """2
2
3
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 3 3 3 3"""
        output = """6
6
6
6
6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
1 2 1 4 2 1 4 1"""
        output = """5
7
5
7
7
5
7
5"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    C = Counter(A)
    S = 0
    for k, v in C.items():
        S += max(v*(v-1)//2, 0)

    for a in A:
        print(S-C[a]+1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
