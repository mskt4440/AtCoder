#
# abc115 b
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
        input = """3
4980
7980
6980"""
        output = """15950"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
4320
4320
4320
4320"""
        output = """15120"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    P = [int(input()) for _ in range(N)]

    print(sum(P)-max(P)//2)


if __name__ == "__main__":
    # unittest.main()
    resolve()
