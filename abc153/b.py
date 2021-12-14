#
# abc153 b
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
        input = """10 3
4 5 6"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 3
4 5 6"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """210 5
31 41 59 26 53"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """211 5
31 41 59 26 53"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))

    if sum(A) >= H:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
