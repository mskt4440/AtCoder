#
# abc027 a
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
        input = """1 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 3 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5 5 5"""
        output = """5"""
        self.assertIO(input, output)


def resolve():
    L = list(map(int, input().split()))
    C = Counter(L)
    print(C.most_common()[-1][0])


if __name__ == "__main__":
    # unittest.main()
    resolve()
