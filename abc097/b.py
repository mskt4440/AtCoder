#
# abc097 b
#
import sys
from io import StringIO
import unittest
import math


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
        input = """10"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999"""
        output = """961"""
        self.assertIO(input, output)


def resolve():
    X = int(input())

    ans = 1
    for i in range(2, math.ceil(math.sqrt(X))+1):
        b = 2
        while i**b <= X:
            b += 1
        ans = max(ans, i**(b-1))

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
