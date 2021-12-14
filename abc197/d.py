#
# abc197 d
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
        input = """4
1 1
2 2"""
        output = """2.00000000000 1.00000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
5 3
7 4"""
        output = """5.93301270189 2.38397459622"""
        self.assertIO(input, output)


def resolve():


if __name__ == "__main__":
    unittest.main()
    # resolve()
