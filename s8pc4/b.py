#
# s8pc4 b
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

    def test_入力例1(self):
        input = """5 5
3949 3774 3598 3469 3424"""
        output = """1541"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 3
7 4 2 6 4"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """2 2
7 8"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    a0, *A = map(int, input().split())

    ans = float("inf")
    for bit in range(1 << (N-1)):
        if bin(bit).count("1") != K-1:
            continue
        cost = 0
        target = a0+1
        for i, a in enumerate(A):
            if (1 << i) & bit == (1 << i):
                cost += max(0, target-a)
                target = a + max(0, target-a) + 1
            else:
                if a > target:
                    target = a+1
        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
