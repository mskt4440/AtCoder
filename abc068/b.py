#
# abc068 b
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
        input = """7"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """32"""
        output = """32"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100"""
        output = """64"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    ans = 1
    while ans * 2 <= N:
        ans *= 2
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
