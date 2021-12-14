#
# abc105 c
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
        input = """-9"""
        output = """1011"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123456789"""
        output = """11000101011001101110100010101"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    ans = ""
    if N == 0:
        ans = "0"
    else:
        while N != 0:
            if N % 4 == 0:
                ans = "00" + ans
            elif N % 4 == 1:
                ans = "01" + ans
                N -= 1
            elif N % 4 == 2:
                ans = "10" + ans
                N += 2
            elif N % 4 == 3:
                ans = "11" + ans
                N += 1
            N //= 4
        if ans[0] == "0":
            ans = ans[1:]

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
