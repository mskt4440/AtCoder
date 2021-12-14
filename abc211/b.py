#
# abc211 b
#
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
        input = """3B
HR
2B
H"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2B
3B
HR
3B"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    S = [input() for _ in range(4)]

    if "H" in S and "2B" in S and "3B" in S and "HR" in S:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
