#
# abc112 b
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
        input = """3 70
7 60
1 80
4 50"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
1 1000
2 4
3 1000
4 500"""
        output = """TLE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 9
25 8
5 9
4 10
1000 1000
6 1"""
        output = """5"""
        self.assertIO(input, output)


def resolve():
    N, T = map(int, input().split())
    CT = [list(map(int, input().split())) for _ in range(N)]

    ans = float("inf")
    for ct in CT:
        c, t = ct
        if t > T:
            continue
        ans = min(ans, c)

    if ans == float("inf"):
        ans = "TLE"

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
