#
# abc021 a
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
        input = """5"""
        output = """3
1
2
2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1"""
        output = """1
1"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    K = 0
    A = []

    if N % 2:
        K += 1
        A.append(1)
        N -= 1
    while N:
        K += 1
        A.append(2)
        N -= 2

    print(K)
    for a in A:
        print(a)


if __name__ == "__main__":
    # unittest.main()
    resolve()
