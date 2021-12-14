#
# abc136 d
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
        input = """RRLRL"""
        output = """0 1 2 1 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """RRLLLLRLRRLL"""
        output = """0 3 3 0 0 0 1 1 0 2 2 0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """RRRLLRLLRRRLLLLL"""
        output = """0 0 3 2 0 2 1 0 0 0 4 4 0 0 0 0"""
        self.assertIO(input, output)


def resolve():
    S = input()

    N = len(S)
    ans = [0]*N
    cnt = 0
    for i in range(N):
        if S[i] == "R":
            cnt += 1
            continue
        else:
            ans[i] += cnt//2
            ans[i-1] += cnt - cnt//2
            cnt = 0

    cnt = 0
    for i in reversed(range(N)):
        if S[i] == "L":
            cnt += 1
            continue
        else:
            ans[i] += cnt//2
            ans[i+1] += cnt - cnt//2
            cnt = 0

    print(*ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
