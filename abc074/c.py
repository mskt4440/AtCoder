#
# abc074 c
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
        input = """1 2 10 20 15 200"""
        output = """110 10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 1 2 100 1000"""
        output = """200 100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """17 19 22 26 55 2802"""
        output = """2634 934"""
        self.assertIO(input, output)


def resolve():
    A, B, C, D, E, F = map(int, input().split())
    N = 0
    W = 100*A
    S = 0
    for i in range(31):
        for j in range(31):
            for k in range(101):
                for l in range(101):
                    w = A*i+B*j
                    s = C*k+D*l
                    if w == 0 or 100*w+s > F or s > w*E:
                        break
                    n = 100*s / (100*w+s)
                    if n > N:
                        N = n
                        W = 100*w+s
                        S = s
    print(f"{W} {S}")


if __name__ == "__main__":
    # unittest.main()
    resolve()
