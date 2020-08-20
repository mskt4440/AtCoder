#
# agc027 a
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
        input = """3 70
20 30 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 10
20 30 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 1111
1 10 100 1000"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 10
20 20"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(N-1):
        if x - a[i] >= 0:
            x -= a[i]
            ans += 1
    if a[-1] == x:
        ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
