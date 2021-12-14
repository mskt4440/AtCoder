#
#  abc195 B
#
import unittest
from io import StringIO
import sys


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
        input = """100 200 2"""
        output = """10 20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """120 150 2"""
        output = """14 16"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """300 333 1"""
        output = """UNSATISFIABLE"""
        self.assertIO(input, output)


def resolve():
    A, B, W = map(int, input().split())

    m = 1000001
    M = 0
    for i in range(1000*1000+1):
        if A*i <= W*1000 <= B*i:
            m = min(m, i)
            M = max(M, i)
    if M == 0:
        print("UNSATISFIABLE")
    else:
        print(m, M)


if __name__ == "__main__":
    # unittest.main()
    resolve()
