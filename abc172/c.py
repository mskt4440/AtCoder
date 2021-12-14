#
# abc172 c
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
        input = """3 4 240
60 90 120
80 150 80 150"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 730
60 90 120
80 150 80 150"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 4 1
1000000000 1000000000 1000000000 1000000000 1000000000
1000000000 1000000000 1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    SA, SB = [0], [0]
    for a in A:
        SA.append(SA[-1]+a)
    for b in B:
        SB.append(SB[-1]+b)

    ans, j = 0, M
    for i in range(N+1):
        if SA[i] > K:
            break
        while SB[j] > K-SA[i]:
            j -= 1

        ans = max(ans, i+j)

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
