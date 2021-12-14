#
# abc198 e
#
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
        input = """6
2 7 1 8 2 8
1 2
3 6
3 2
4 3
2 5"""
        output = """1
2
3
4
6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10"""
        output = """1
2
3
5
6
7
8"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    C = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(N-1)]

    G = [[]*N for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)


if __name__ == "__main__":
    # unittest.main()
    # resolve()
