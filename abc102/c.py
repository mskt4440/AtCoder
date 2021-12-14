#
# abc102 c
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
        input = """5
2 2 3 5 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
1 2 3 4 5 6 7 8 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
6 5 4 3 2 1"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7
1 1 1 1 2 3 4"""
        output = """6"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    B = []
    for i, a in enumerate(A, 1):
        B.append(a-i)
    B.sort()
    M = B[(N-1)//2]
    ans = sum([abs(b-M) for b in B])

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
