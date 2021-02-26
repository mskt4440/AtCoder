#
# abc121 b
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
        input = """2 3 -10
1 2 3
3 2 1
1 2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2 -4
-2 5
100 41
100 40
-3 0
-6 -2
18 -13"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3 0
100 -100 0
0 100 100
100 100 100
-100 100 100"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for AI in A:
        t = 0
        for i in range(M):
            t += AI[i]*B[i]
        if t + C > 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
