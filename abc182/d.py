#
# abc182 d
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
        input = """3
2 -1 -2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
-2 1 3 -1 -1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
-1000 -1000 -1000 -1000 -1000"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    SA = [0]*N
    for i, a in enumerate(A):
        if i == 0:
            SA[i] = a
        else:
            SA[i] = SA[i-1] + a

    MA = [0]*N
    for i, sa in enumerate(SA):
        if i == 0:
            MA[0] = sa
        else:
            if sa > MA[i-1]:
                MA[i] = sa
            else:
                MA[i] = MA[i-1]

    ans = 0
    c = 0
    for i, a in enumerate(A):
        ans = max(ans, c + MA[i])
        c += SA[i]

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
