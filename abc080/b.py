#
# abc080 b
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
        input = """12"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """57"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """148"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N = input()
    s = 0
    for i in range(len(N)):
        s += int(N[i])
    if int(N) % s == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
