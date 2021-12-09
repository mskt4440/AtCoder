#
# abc050 c
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
        input = """5
2 4 4 0 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
6 4 0 2 4 0 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
7 5 1 1 7 3 5 3"""
        output = """16"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    B = []
    for i in range(N):
        B.append(abs(N-(2*i+1)))

    if sorted(A) != sorted(B):
        print(0)
    elif N % 2:
        print(2**((N-1)//2) % (10**9+7))
    else:
        print(2**(N//2) % (10**9+7))


if __name__ == "__main__":
    # unittest.main()
    resolve()
