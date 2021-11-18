#
# abc025 b
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
        input = """3 5 10
East 7
West 3
West 11"""
        output = """West 8"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3 8
West 6
East 3
East 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5 25 25
East 1
East 1
West 1
East 100
West 1"""
        output = """East 25"""
        self.assertIO(input, output)


def resolve():
    N, A, B = map(int, input().split())
    SD = [input().split() for _ in range(N)]

    p = 0
    for s, d in SD:
        d = int(d)
        if d < A:
            d = A
        elif d > B:
            d = B

        if s == "East":
            p += d
        else:
            p -= d

    if p > 0:
        print("East " + str(p))
    elif p < 0:
        print("West " + str(-p))
    else:
        print("0")


if __name__ == "__main__":
    # unittest.main()
    resolve()
