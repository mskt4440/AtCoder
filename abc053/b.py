#
# abc053 b
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
        input = """QWERTYASDFZXCV"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ZABCZ"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """HASFJGHOGAKZZFEGA"""
        output = """12"""
        self.assertIO(input, output)


def resolve():
    s = input()
    print(s.rfind("Z") - s.find("A") + 1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
