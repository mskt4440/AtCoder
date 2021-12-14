#
# abc152 c
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
        input = """5
4 2 5 1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
4 3 2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
5 7 4 2 6 8 1 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1
1"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    P = list(map(int, input().split()))

    ans = 1
    m = P[0]
    for p in P[1:]:
        if p > m:
            continue
        ans += 1
        m = min(p, m)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
