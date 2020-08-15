#
# abc049 c
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
        input = """erasedream"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """dreameraser"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """dreamerer"""
        output = """NO"""
        self.assertIO(input, output)


def resolve():
    W = ["dream", "dreamer", "erase", "eraser"]
    for i in range(4):
        W[i] = W[i][::-1]
    S = input()
    S = S[::-1]
    ans = "NO"
    while True:
        if S == "":
            ans = "YES"
            break
        for i in range(4):
            if S.find(W[i]) == 0:
                S = S[len(W[i]):]
                break
        else:
            break
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
