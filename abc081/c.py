#
# abc081 c
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
        input = """5 2
1 1 2 2 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 1 2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 3
5 1 3 2 4 1 1 2 3 4"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    an = [0] * N
    for i in a:
        an[i-1] += 1
    an.sort(reverse=True)
    ans = 0
    for i in an:
        if K == 0:
            ans += i
        else:
            K -= 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
