#
# agc025 a
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
        input = """15"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000"""
        output = """10"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    ans = float('inf')
    for a in range(1, N):
        b = N - a
        A = str(a)
        B = str(b)
        t = 0
        for i in range(len(A)):
            t += int(A[i])
        for i in range(len(B)):
            t += int(B[i])
        ans = min(ans, t)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
