#
# abc194 b
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
        input = """3
8 5
4 4
7 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
11 7
3 2
6 7"""
        output = """5"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append([i, a])
        B.append([i, b])

    A.sort(key=lambda x: x[1])
    B.sort(key=lambda x: x[1])

    if A[0][0] != B[0][0]:
        print(max(A[0][1], B[0][1]))
    else:
        print(min(A[0][1]+B[0][1], max(A[0][1], B[1][1]), max(A[1][1], B[0][1])))


if __name__ == "__main__":
    # unittest.main()
    resolve()
