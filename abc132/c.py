#
# abc132 c
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
        input = """6
9 1 4 4 6 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
9 1 14 5 5 4 4 14"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """14
99592 10342 29105 78532 83018 11639 92015 77204 30914 21912 34519 80835 100000 1"""
        output = """42685"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    D = list(map(int, input().split()))

    D.sort()
    if D[N//2-1] == D[N//2]:
        print("0")
    else:
        print(D[N//2]-D[N//2-1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
