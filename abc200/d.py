#
# abc200 d
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
180 186 189 191 218"""
        output = """Yes
1 1
2 3 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
123 523"""
        output = """Yes
1 1
1 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
2013 1012 2765 2021 508 6971"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    S = []
    for a in A:
        S.append(a % 200)

    for i in range(201):


if __name__ == "__main__":
    unittest.main()
    # resolve()
