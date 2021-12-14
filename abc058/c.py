#
# abc058 c
#
import sys
from io import StringIO
import unittest
from collections import Counter


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
        input = """3
cbaa
daacc
acacac"""
        output = """aac"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
a
aa
b"""
        output = """"""
        self.assertIO(input, output)


def resolve():
    n = int(input())
    S = [list(input()) for _ in range(n)]

    abc = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for i in range(26):
        an = float("inf")
        for s in S:
            an = min(an, s.count(abc[i]))
        ans += abc[i]*an

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
