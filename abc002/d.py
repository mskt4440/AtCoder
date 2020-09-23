#
# abc002 d
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
        input = """5 3
1 2
2 3
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3
1 2
2 3
3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 9
1 2
1 3
2 3
4 5
4 6
4 7
5 6
5 7
6 7"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """12 0"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(M)]

    ans = 1
    for bit in range(1 << N):
        n = bin(bit).count("1")
        if n < 2:
            continue
        l = 0
        for xy in XY:
            x, y = xy
            if 1 << (x-1) & bit == 1 << (x-1) and 1 << (y-1) & bit == 1 << (y-1):
                l += 1
        if n*(n-1)/2 == l:
            ans = max(ans, n)

    print(ans)


if __name__ == "__main__":
    unittest.main()
    # resolve()
