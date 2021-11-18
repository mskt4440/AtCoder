#
# abc022 a
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
        input = """5 60 70
50
10
10
10
10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 50 100
120
-10
-20
-30
70"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    N, S, T = map(int, input().split())
    W = int(input())
    A = [0]
    for _ in range(N-1):
        A.append(int(input()))

    w = W
    ans = 0
    for a in A:
        w += a
        if S <= w <= T:
            ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
