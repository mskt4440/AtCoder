#
# abc041 c
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
        input = """3
140 180 160"""
        output = """2
3
1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2
1000000000 1"""
        output = """1
2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """8
3 1 4 15 9 2 6 5"""
        output = """4
5
7
8
3
1
6
2"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    L = []
    for i, a in enumerate(A):
        L.append([i, a])
    L.sort(key=lambda x: x[1], reverse=True)

    for i, a in L:
        print(i+1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
