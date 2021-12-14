#
# abc122 c
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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)


def resolve():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]

    AC = [0]*N
    n = S.count("AC")
    AC[0] = n
    for i in range(1, N):
        if S[i-1:i+1] == "AC":
            n -= 1
        AC[i] = n

    for lr in LR:
        l, r = lr
        print(AC[l-1]-AC[r-1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
