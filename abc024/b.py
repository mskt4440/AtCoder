#
# abc024 b
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
        input = """5 10
20
100
105
217
314"""
        output = """45"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """10 10
1
2
3
4
5
6
7
8
9
10"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 100000
3
31
314
3141
31415
314159
400000
410000
500000
777777"""
        output = """517253"""
        self.assertIO(input, output)


def resolve():
    N, T = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    ans = N*T
    for i in range(N-1):
        d = A[i+1] - A[i]
        if d < T:
            ans -= T-d
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
