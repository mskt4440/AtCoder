#
# abc084 d
#
import sys
from io import StringIO
import unittest
from unittest.signals import removeHandler


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
        input = """1
3 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
13 13
7 11
7 11
2017 2017"""
        output = """1
0
0
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 53
13 91
37 55
19 51
73 91
13 49"""
        output = """4
4
1
1
1
2"""
        self.assertIO(input, output)


def resolve():
    Q = int(input())
    LR = [list(map(int, input().split())) for _ in range(Q)]

    A = list(range(2, 100000))
    P = []
    while A[0]**2 <= 100000:
        tmp = A[0]
        P.append(tmp)
        A = [a for a in A if a % tmp]
    P = P+A
    P = set(P)

    C = [0]*100000
    for i in range(3, 100000):
        if i in P and (i+1)//2 in P:
            C[i] += 1

    for i in range(3, 100000):
        C[i] += C[i-1]

    for l, r in LR:
        print(C[r]-C[l-1])


if __name__ == "__main__":
    unittest.main()
    # resolve()
