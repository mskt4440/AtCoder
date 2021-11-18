#
# abc018 b
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
        input = """abcdef
2
3 5
1 4"""
        output = """debacf"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """redcoat
3
1 7
1 2
3 4"""
        output = """atcoder"""
        self.assertIO(input, output)


def resolve():
    S = input()
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]

    ans = S
    for l, r in LR:
        ans = ans[:l-1] + ans[l-1:r][::-1] + ans[r:]

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
