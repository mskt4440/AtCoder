#
# abc027 b
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
        input = """3
1 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
2 0 0 0 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """2
0 99"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4
0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    T = sum(A)

    if T % N:
        print(-1)
    else:
        ave = T//N
        ans = 0
        for i in range(N-1):
            if sum(A[:i+1]) != ave*(i+1):
                ans += 1

        print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
