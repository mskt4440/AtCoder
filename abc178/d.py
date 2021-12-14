#
# abc178 d
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
        input = """7"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1729"""
        output = """294867501"""
        self.assertIO(input, output)


def resolve():
    S = int(input())

    ans = solve(S) % (10**9+7)
    print(ans)


def solve(n):
    if n < 3:
        return 0
    elif n < 6:
        return 1
    return solve(n-3)*2+1


if __name__ == "__main__":
    unittest.main()
    # resolve()
