#
# abc196 c
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
        input = """33"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1333"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000"""
        output = """999"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    ans = 0
    x = 1
    while int(str(x)*2) <= N:
        ans += 1
        x += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
