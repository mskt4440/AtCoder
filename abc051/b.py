#
# abc051 b
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
        input = """2 2"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 15"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    K, S = map(int, input().split())
    ans = 0
    for i in range(K+1):
        for j in range(K+1):
            if 0 <= S-i-j <= K:
                ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
