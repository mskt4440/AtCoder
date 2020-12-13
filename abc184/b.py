#
# abc184 b
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
        input = """3 0
xox"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 199999
oooooooooxoooooooooo"""
        output = """200017"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 10
xxxxxxxxxxxxxxxxxxxx"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N, X = map(int, input().split())
    S = input()

    ans = X
    for i in range(N):
        if S[i] == "o":
            ans += 1
        elif ans > 0:
            ans -= 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
