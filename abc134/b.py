#
# abc134 b
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
        input = """6 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 4"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N, D = map(int, input().split())

    print((N+2*D)//(2*D+1))


if __name__ == "__main__":
    # unittest.main()
    resolve()
