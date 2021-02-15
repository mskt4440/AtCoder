#
# abc115 d
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
        input = """2 7"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """50 4321098765432109"""
        output = """2160549382716056"""
        self.assertIO(input, output)


def resolve():
    N, X = map(int, input().split())

    global a, p
    a = [1]
    p = [1]
    for i in range(N):
        a.append(a[i] * 2 + 3)
        p.append(p[i] * 2 + 1)

    print(f(N, X))


def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + a[N-1]:
        return f(N-1, X-1)
    else:
        return p[N-1] + 1 + f(N-1, X-2-a[N-1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
