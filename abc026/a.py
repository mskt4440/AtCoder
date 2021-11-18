#
# abc026 a
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

    def test_入力例1(self):
        input = """10"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """60"""
        output = """900"""
        self.assertIO(input, output)


def resolve():
    A = int(input())
    print(A//2 * A//2)


if __name__ == "__main__":
    # unittest.main()
    resolve()
