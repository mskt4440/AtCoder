#
# abc094 b
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
        input = """5 3 3
1 2 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 3 2
4 5 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 7 5
1 2 3 4 6 8 9"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans1 = 0
    for x in range(X, N+1):
        for a in A:
            if x == a:
                ans1 += 1
                break

    ans2 = 0
    for x in range(X, -1, -1):
        for a in A:
            if x == a:
                ans2 += 1
                break

    print(min(ans1, ans2))


if __name__ == "__main__":
    # unittest.main()
    resolve()
