#
# abc141 c
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
        input = """6 3 4
3
1
3
2"""
        output = """No
No
Yes
No
No
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5 4
3
1
3
2"""
        output = """Yes
Yes
Yes
Yes
Yes
Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 13 15
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9"""
        output = """No
No
No
No
Yes
No
No
No
Yes
No"""
        self.assertIO(input, output)


def resolve():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    S = [K-Q]*N

    for a in A:
        S[a-1] += 1

    for s in S:
        if s > 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
