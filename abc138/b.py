#
# abc138 b
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
10 30"""
        output = """7.5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
200 200 200"""
        output = """66.66666666666667"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1000"""
        output = """1000"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for a in A:
        ans += 1/a

    print(1/ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
