#
# abc018 a
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
        input = """12
18
11"""
        output = """2
1
3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """10
20
30"""
        output = """3
2
1"""
        self.assertIO(input, output)


def resolve():
    L = [int(input()) for _ in range(3)]
    L_sorted = sorted(L, reverse=True)
    for i in range(3):
        print(L_sorted.index(L[i])+1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
