#
# abc141 d
#
from heapq import heapify
import sys
from io import StringIO
import unittest
import heapq


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
        input = """3 3
2 13 8"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 9 3 5"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 100000
1000000000"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """9500000000"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A = list(map(lambda x: x*(-1), A))
    heapq.heapify(A)

    for _ in range(M):
        m = heapq.heappop(A) * (-1)
        heapq.heappush(A, m//2*(-1))

    print(sum(A)*(-1))


if __name__ == "__main__":
    # unittest.main()
    resolve()
