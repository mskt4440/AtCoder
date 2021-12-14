#
# abc139 c
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
10 4 8 7 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
4 4 5 6 6 5 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    H = list(map(int, input().split()))

    n = H[0]
    ans = 0
    tmp = 0
    for h in H[1:]:
        if h > n:
            ans = max(ans, tmp)
            tmp = 0
        else:
            tmp += 1
        n = h

    ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
