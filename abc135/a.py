#
# abc135 a
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
        input = """2 16"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 3"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """998244353 99824435"""
        output = """549034394"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    if (A+B) % 2:
        print("IMPOSSIBLE")
    else:
        print((A+B)//2)


if __name__ == "__main__":
    # unittest.main()
    resolve()
