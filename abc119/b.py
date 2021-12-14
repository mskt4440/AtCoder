#
# abc119 b
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
        input = """2
10000 JPY
0.10000000 BTC"""
        output = """48000.0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
100000000 JPY
100.00000000 BTC
0.00000001 BTC"""
        output = """138000000.0038"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    ans = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            ans += int(x)
        else:
            ans += float(x)*380000
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
