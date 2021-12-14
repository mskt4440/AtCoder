#
# abc164 b
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
        input = """10 9 10 10"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """46 4 40 5"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    A, B, C, D = map(int, input().split())

    t = (A+D-1)//D
    a = (C+B-1)//B

    if t >= a:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
