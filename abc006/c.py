#
# abc006 c
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
        input = """3 9"""
        output = """1 1 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 23"""
        output = """1 3 3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 41"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())

    if M < N*2 or N*4 < M:
        print("-1 -1 -1")
    else:
        for z in range(N+1):
            y = M - 2*N - 2*z
            x = 3*N + z - M
            if x < 0 or N < x or y < 0 or N < y:
                continue
            print(x, y, z)
            break


if __name__ == "__main__":
    # unittest.main()
    resolve()
