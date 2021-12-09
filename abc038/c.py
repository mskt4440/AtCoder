#
# abc038 c
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
        input = """5
1 2 3 2 1"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
1 2 3 4"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6
3 3 4 1 2 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """6
1 5 2 3 4 2"""
        output = """10"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = N
    c = 1
    for i in range(1, N):
        if A[i] > A[i-1]:
            c += 1
        else:
            c = 1
        ans += c-1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
