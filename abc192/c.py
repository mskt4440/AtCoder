#
# abc192 c
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
        input = """314 2"""
        output = """693"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6174 100000"""
        output = """6174"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())

    ans = N
    for i in range(K):
        ans = f(ans)

    print(ans)


def f(n):
    l = list(str(n))
    ll = sorted(l)
    gl = ll[::-1]

    sgl = ""
    sll = ""
    for s in gl:
        sgl += s
    for s in ll:
        sll += s

    return int(sgl) - int(sll)


if __name__ == "__main__":
    # unittest.main()
    resolve()
