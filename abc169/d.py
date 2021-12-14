#
# abc169 d
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
        input = """24"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """64"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1000000007"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """997764507000"""
        output = """7"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    i = 2
    D = dict()
    n = N
    while i*i <= N:
        while n % i == 0:
            n = n//i
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        i += 1
    if n != 1:
        D[n] = 1

    ans = 0
    for p, e in D.items():
        for i in range(1, e+1):
            z = p**i
            if N % z == 0:
                N //= z
                ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
