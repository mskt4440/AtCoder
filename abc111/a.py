#
# abc111 a
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
        input = """119"""
        output = """991"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """999"""
        output = """111"""
        self.assertIO(input, output)


def resolve():
    N = input()
    for n in N:
        if n == "1":
            print("9", end="")
        elif n == "9":
            print("1", end="")
        else:
            print(n, end="")
    print()


if __name__ == "__main__":
    # unittest.main()
    resolve()
