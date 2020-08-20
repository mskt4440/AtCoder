#
# agc012 a
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
5 2 8 5 1 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """10000000000"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(N):
        a.pop()
        ans += a.pop()
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
