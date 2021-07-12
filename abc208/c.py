#
# abc208 c
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
        input = """2 7
1 8"""
        output = """4
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 3
33"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 1000000000000
99 8 2 4 43 5 3"""
        output = """142857142857
142857142857
142857142858
142857142857
142857142857
142857142857
142857142857"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    B = []
    for i, a in enumerate(A):
        B.append([i, a])
    B.sort(key=lambda x: x[1])

    if K >= N:
        ANS = [K//N]*N
        K = K % N
    else:
        ANS = [0]*N

    for i, a in B:
        if K > 0:
            ANS[i] += 1
            K -= 1

    for ans in ANS:
        print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
