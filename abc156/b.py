#
# abc156 b
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
        input = """11 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1010101 10"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265 3"""
        output = """18"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())

    ans = 0
    while N:
        N //= K
        ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
