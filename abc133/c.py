#
# abc133 c
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
        input = """2020 2040"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5"""
        output = """20"""
        self.assertIO(input, output)


def resolve():
    L, R = map(int, input().split())

    ans = L * R % 2019
    if R - L >= 2019:
        ans = 0
    else:
        for i in range(L, R+1):
            for j in range(i+1, R+1):
                ans = min(ans, i*j % 2019)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
