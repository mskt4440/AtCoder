#
# abc118 b
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
        input = """3 4
2 1 3
3 1 2 3
2 3 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
4 2 3 4 5
4 1 3 4 5
4 1 2 4 5
4 1 2 3 5
4 1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 30
3 5 10 30"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    KA = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(1, M+1):
        t = 0
        for k, *A in KA:
            if i in set(A):
                t += 1
        else:
            if t == N:
                ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
