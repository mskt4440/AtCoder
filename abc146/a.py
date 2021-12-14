#
# abc146 a
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
        input = """SAT"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """SUN"""
        output = """7"""
        self.assertIO(input, output)


def resolve():
    S = input()
    W = {"SUN": 7, "MON": 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1}

    print(W[S])


if __name__ == "__main__":
    # unittest.main()
    resolve()
