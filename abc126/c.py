#
# abc126 c
#
import sys
from io import StringIO
import unittest
import math


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
        input = """3 10"""
        output = """0.145833333333"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000 5"""
        output = """0.999973749998"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())

    ans = 0
    for i in range(N):
        if i+1 >= K:
            ans += 1
        else:
            ans += (1/2)**math.ceil(math.log2(K/(i+1)))

    print(ans/N)


if __name__ == "__main__":
    # unittest.main()
    resolve()
