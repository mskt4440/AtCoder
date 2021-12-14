#
# abc205 d
#
import sys
from io import StringIO
import unittest
import bisect


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
3 5 6 7
2
5
3"""
        output = """2
9
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
1 2 3 4 5
1
10"""
        output = """6
15"""
        self.assertIO(input, output)


def resolve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    mi = A[0]
    mx = A[-1]
    for _ in range(Q):
        k = int(input())
        if k < mi:
            print(k)
        elif mx < k:
            print(k+len(A))
        else:
            i = bisect.bisect_left(A, k)


if __name__ == "__main__":
    unittest.main()
    # resolve()
