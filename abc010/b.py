#
# abc010 b
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
5 8 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """9
1 2 3 4 5 6 7 8 9"""
        output = """8"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    n = [0]*9
    for i in range(1, 10):
        p = i
        while p % 2 == 0 or p % 3 == 2:
            p -= 1
        n[i-1] = i-p

    ans = 0
    for a in A:
        ans += n[a-1]

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
