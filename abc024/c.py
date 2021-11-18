#
# abc024 c
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

    def test_入力例1(self):
        input = """10 10 3
1 5
3 6
7 10
5 8
4 4
1 4
2 9
1 3
1 1
4 5
1 6
2 7
10 1"""
        output = """2
4
8"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """10 10 4
1 2
2 4
3 6
4 8
5 10
9 10
7 8
5 6
3 5
1 3
10 1
3 8
2 4
1 3"""
        output = """10
4
2
2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """314159265 10 1
1 10000
500 12031
1414 113232
111111 777777
666661 23423423
12345678 123456789
111111111 314159265
112334 235235235
1 223445
314 1592
1 314159265"""
        output = """7"""
        self.assertIO(input, output)


def resolve():
    N, D, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(D)]
    ST = [list(map(int, input().split())) for _ in range(K)]

    x = [0]*K
    t = [0]*K
    ans = [0]*K
    for i in range(K):
        x[i] = ST[i][0]
        t[i] = ST[i][1]

    for d, lr in enumerate(LR):
        l = lr[0]
        r = lr[1]
        for i in range(K):
            if x[i] != t[i] and l <= x[i] <= r:
                if l <= t[i] <= r:
                    ans[i] = d+1
                    x[i] = t[i]
                elif t[i] < l:
                    x[i] = l
                else:
                    x[i] = r

    for i in range(K):
        print(ans[i])


if __name__ == "__main__":
    # unittest.main()
    resolve()
