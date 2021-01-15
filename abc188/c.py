#
# abc188 c
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
        input = """2
1 4 2 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
3 1 5 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    mxi = A.index(max(A))
    if mxi < 2**(N-1):
        print(A.index(max(A[2**(N-1):]))+1)
    else:
        print(A.index(max(A[:2**(N-1)]))+1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
