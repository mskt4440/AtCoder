#
# abc123 b
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
        input = """29
20
7
35
120"""
        output = """215"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """101
86
119
108
57"""
        output = """481"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123
123
123
123
123"""
        output = """643"""
        self.assertIO(input, output)


def resolve():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    L = [a, b, c, d, e]
    A = []
    B = []
    for l in L:
        if l % 10:
            A.append(l)
        else:
            B.append(l)
    A.sort(key=lambda x: x % 10, reverse=True)

    ans = 0
    if len(A):
        for a in A[:-1]:
            ans += a + (10-a % 10)
        print(ans+A[-1]+sum(B))
    else:
        print(sum(B))


if __name__ == "__main__":
    # unittest.main()
    resolve()
