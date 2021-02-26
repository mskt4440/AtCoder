#
# abc121 c
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
        input = """2 5
4 9
2 4"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 30
6 18
2 5
3 10
7 9"""
        output = """130"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 100000
1000000000 100000"""
        output = """100000000000000"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    AB.sort()
    ans = 0
    n = 0
    for a, b in AB:
        if b < M-n:
            n += b
            ans += a*b
        else:
            ans += a*(M-n)
            break
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
