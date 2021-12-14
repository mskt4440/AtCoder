#
#  abc198 B
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
        input = """1210"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """777"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123456789"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N = input()

    ans = "No"
    for i in range(len(N)):
        T = "0"*i+N
        if T == T[::-1]:
            ans = "Yes"
            break

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
