#
# abcw201 a
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
        input = """5 1 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 4 3"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5 5"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    A = list(map(int, input().split()))
    A.sort()

    if A[1]-A[0] == A[2]-A[1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
