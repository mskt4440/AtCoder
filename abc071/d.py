#
# abc071 d
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
        input = """3
aab
ccb"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
Z
Z"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """52
RvvttdWIyyPPQFFZZssffEEkkaSSDKqcibbeYrhAljCCGGJppHHn
RLLwwdWIxxNNQUUXXVVMMooBBaggDKqcimmeYrhAljOOTTJuuzzn"""
        output = """958681902"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S1 = input()
    S2 = input()

    ans = 0
    i = 0
    p = 0
    while i < N:
        if S1[i] == S2[i]:
            if p == 0:
                ans = 3
            elif p == 1:
                ans *= 2
            p = 1
            i += 1
            continue
        else:
            if p == 0:
                ans = 6
            elif p == 1:
                ans *= 2
            else:
                ans *= 3
            p = 2
            i += 2

    print(ans % 1000000007)


if __name__ == "__main__":
    # unittest.main()
    resolve()
