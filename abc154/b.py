#
# abc154 b
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
        input = """sardine"""
        output = """xxxxxxx"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """xxxx"""
        output = """xxxx"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """gone"""
        output = """xxxx"""
        self.assertIO(input, output)


def resolve():
    S = input()

    print("x"*len(S))


if __name__ == "__main__":
    # unittest.main()
    resolve()
