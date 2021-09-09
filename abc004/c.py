#
# abc004 c
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
        input = """1"""
        output = """213456"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5"""
        output = """234561"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """22"""
        output = """615234"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000000"""
        output = """345612"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    N = N % 30
    ans = list(range(1, 7))
    for i in range(N):
        x = i % 5
        ans[x], ans[x+1] = ans[x+1], ans[x]

    print(*ans, sep="")


if __name__ == "__main__":
    # unittest.main()
    resolve()
