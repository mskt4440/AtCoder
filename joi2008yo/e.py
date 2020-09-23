#
# joi2008yo e
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
0 1 0 1 0
1 0 0 0 1"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 6
1 0 0 0 1 0
1 1 1 0 1 0
1 0 1 1 0 1"""
        output = """15"""
        self.assertIO(input, output)


def resolve():
    R, C = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(R)]
    A_rev = [[1 - v for v in a] for a in A]

    ans = 0
    for bit in range(1 << R):
        num = 0
        T = A[:]
        for i, t in enumerate(T):
            if 1 << i & bit:
                T[i] = A_rev[i]

        T = list(zip(*T))
        for t in T:
            num += max(sum(t), R-sum(t))
        ans = max(ans, num)

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
