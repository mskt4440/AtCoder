#
# abc192 d
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
        input = """22
10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """999
1500"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000000000000000000000000000000000000000000000000000000000
1000000000000000000"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    X = input()
    M = int(input())

    if len(X) == 1:
        if int(X) > M:
            print(0)
        else:
            print(1)
    else:
        d = int(max(X))
        l = d
        r = M+1

        while abs(r-l) > 1:
            m = (l+r)//2
            if base10from(X, m) >= M:
                r = m
            else:
                l = m

        if base10from(X, r) > M:
            r -= 1

        print(max(0, r-d))


def base10from(num, b):
    n = 0
    numlist = list(num)
    while (numlist):
        n *= b
        n += int(numlist.pop(0))
    return n


if __name__ == "__main__":
    # unittest.main()
    resolve()
