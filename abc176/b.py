#
# abc176 b
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
        input = """123456789"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31415926535897932384626433832795028841971693993751058209749445923078164062862089986280"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N = input()

    S = 0
    for i in range(len(N)):
        S += int(N[i])
    if S % 9 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
