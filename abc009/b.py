#
# abc009 b
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

    def test_入力例1(self):
        input = """4
100
200
300
300"""
        output = """200"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
50
370
819
433
120"""
        output = """433"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6
100
100
100
200
200
200"""
        output = """100"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    A = sorted(list(set(A)), reverse=True)
    print(A[1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
