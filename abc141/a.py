#
# abc141 a
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
        input = """Sunny"""
        output = """Cloudy"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """Rainy"""
        output = """Sunny"""
        self.assertIO(input, output)


def resolve():
    S = input()

    if S == "Sunny":
        print("Cloudy")
    elif S == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")


if __name__ == "__main__":
    # unittest.main()
    resolve()
