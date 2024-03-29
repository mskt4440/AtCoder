#
# abc162 a
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
        input = """117"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """777"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    N = input()

    if N[0] == "7" or N[1] == "7" or N[2] == "7":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
