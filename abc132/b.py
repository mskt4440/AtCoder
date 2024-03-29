#
# abc132 b
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
1 3 5 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
9 6 3 2 5 8 7 4 1"""
        output = """5"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    P = list(map(int, input().split()))

    ans = 0
    for i in range(N-2):
        if P[i] < P[i+1] < P[i+2] or P[i] > P[i+1] > P[i+2]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
