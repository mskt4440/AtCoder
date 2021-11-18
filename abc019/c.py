#
# abc019 c
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

    def test_入力例1(self):
        input = """3
1 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
2 4 8 16"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4
2 3 5 7"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N):
        while True:
            if A[i] % 2:
                break
            A[i] //= 2
    print(len(set(A)))


if __name__ == "__main__":
    # unittest.main()
    resolve()
