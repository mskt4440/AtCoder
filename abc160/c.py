#
# abc160 c
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
        input = """20 3
5 10 15"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 3
0 5 15"""
        output = """10"""
        self.assertIO(input, output)


def resolve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    D = []
    for i in range(1, N):
        D.append(A[i]-A[i-1])
    D.append(A[0]+K-A[-1])

    dm = 0
    for d in D:
        dm = max(dm, d)
    print(K-dm)


if __name__ == "__main__":
    # unittest.main()
    resolve()
