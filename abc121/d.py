#
# abc121 d
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
        input = """2 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123 456"""
        output = """435"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123456789012 123456789012"""
        output = """123456789012"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    if A % 2:
        if (B-A) % 4 == 0:
            print(A)
        elif (B-A) % 4 == 1:
            print(A ^ B)
        elif (B-A) % 4 == 2:
            print(A ^ (B-1) ^ B)
        else:
            print(A ^ B ^ 1)
    if A % 2 == 0:
        if (B-A+1) % 4 == 0:
            print(0)
        elif (B-A+1) % 4 == 1:
            print(B)
        elif (B-A+1) % 4 == 2:
            print((B-1) ^ B)
        else:
            print(B ^ 1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
