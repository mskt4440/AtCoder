#
# abc030 b
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
        input = """15 0"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 17"""
        output = """3.5"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """6 0"""
        output = """180"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """23 59"""
        output = """5.5000"""
        self.assertIO(input, output)


def resolve():
    n, m = map(int, input().split())

    N = n % 12*30 + m/2
    M = m*6
    ans = abs(N-M)
    if ans <= 180:
        print(ans)
    else:
        print(360-ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
