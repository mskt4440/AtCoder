#
# abc115 a
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
        input = """25"""
        output = """Christmas"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """22"""
        output = """Christmas Eve Eve Eve"""
        self.assertIO(input, output)


def resolve():
    D = int(input())

    ans = "Christmas"
    if D == 25:
        print(ans)
    elif D == 24:
        print(ans+" Eve")
    elif D == 23:
        print(ans+" Eve Eve")
    elif D == 22:
        print(ans+" Eve Eve Eve")


if __name__ == "__main__":
    # unittest.main()
    resolve()
