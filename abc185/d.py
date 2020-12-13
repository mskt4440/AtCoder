#
# abc185 d
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
        input = """5 2
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """13 3
13 3 9"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
5 2 1 4 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 0"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    if M == 0:
        print("1")
    elif N == M:
        print("0")
    else:
        A = list(map(int, input().split()))
        A.append(0)
        A.append(N+1)
        A.sort()
        k = N
        for i in range(1, M+1):
            k = min(k, max(A[i]-A[i-1]-1, 1))

        ans = 0
        for i in range(1, M+2):
            d = A[i]-A[i-1]-1
            if d == 0:
                continue
            elif d % k == 0:
                ans += d//k
            else:
                ans += d//k+1

        print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
