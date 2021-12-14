#
# abc171 c
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
        input = """2"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """27"""
        output = """aa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123456789"""
        output = """jjddja"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    ans = ""
    while N:
        N -= 1
        ans += chr(ord("a") + N % 26)
        N //= 26
    print(ans[::-1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
