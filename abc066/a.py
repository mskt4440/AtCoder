#
# abc066 a
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
        input = """700 600 780"""
        output = """1300"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10000 10000 10000"""
        output = """20000"""
        self.assertIO(input, output)


def resolve():
    B = list(map(int, input().split()))
    B.sort()

    print(sum(B[:2]))


if __name__ == "__main__":
    # unittest.main()
    resolve()
