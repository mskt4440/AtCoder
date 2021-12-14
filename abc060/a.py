#
# abc060 a
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
        input = """rng gorilla apple"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """yakiniku unagi sushi"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """a a a"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """aaaaaaaaab aaaaaaaaaa aaaaaaaaab"""
        output = """NO"""
        self.assertIO(input, output)


def resolve():
    A, B, C = input().split()

    if A[-1] == B[0] and B[-1] == C[0]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # unittest.main()
    resolve()
