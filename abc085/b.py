#
# abc085 b
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
        input = """4
10
8
8
6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
15
15
15"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
50
30
50
100
50
80
30"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    d = []
    for _ in range(N):
        d.append(int(input()))
    # d.sort()
    #ans = 1
    # for i in range(1, N):
    #    if d[i] > d[i-1]:
    #        ans += 1
    # print(ans)
    n = {}
    for i in range(N):
        n[d[i]] = 1
    print(len(n))


if __name__ == "__main__":
    # unittest.main()
    resolve()
