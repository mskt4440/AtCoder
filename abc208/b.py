#
# abc208 b
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
        input = """9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """119"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000"""
        output = """24"""
        self.assertIO(input, output)


def resolve():
    P = int(input())

    C = [1]
    for i in range(2, P+1):
        if C[-1]*i > P:
            break
        C.append(C[-1]*i)
    C.sort(reverse=True)

    S = 0
    ans = 0
    for c in C:
        if S < P:
            t = (P-S)//c
            S += c*t
            ans += t

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
