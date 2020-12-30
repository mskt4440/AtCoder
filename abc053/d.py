#
# abc053 d
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
1 2 1 3 7"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """15
1 3 5 2 1 3 2 8 8 6 2 6 11 1 1"""
        output = """7"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    SA = set(A)
    la = len(A)
    lsa = len(SA)
    if (la-lsa) % 2:
        print(lsa-1)
    else:
        print(lsa)


if __name__ == "__main__":
    # unittest.main()
    resolve()
