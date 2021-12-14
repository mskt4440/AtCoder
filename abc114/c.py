#
# abc114 c
#
import sys
from io import StringIO
import unittest
from itertools import product, repeat


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
        input = """575"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3600"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999999999"""
        output = """26484"""
        self.assertIO(input, output)


def resolve():
    N = input()

    n = len(N)
    N = int(N)

    ans = 0
    for i in range(3, n+1):
        L = product('357', repeat=i)
        for l in L:
            if "3" in l and "5" in l and "7" in l:
                t = 0
                for i in range(len(l)):
                    t += 10**(len(l)-1-i)*int(l[i])
                if t <= N:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
