#
# abc134 c
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
1
4
3"""
        output = """4
3
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
5
5"""
        output = """5
5"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    SA = sorted(A, reverse=True)
    for a in A:
        if a == SA[0]:
            print(SA[1])
        else:
            print(SA[0])


if __name__ == "__main__":
    # unittest.main()
    resolve()
