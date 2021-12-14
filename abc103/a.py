#
# abc103 a
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
        input = """1 6 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11 5 5"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 100 100"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    A = list(map(int, input().split()))

    ans = float("inf")
    for i in range(3):
        tmp = 0
        for j in range(3):
            if i == j:
                continue
            tmp += abs(A[j]-A[i])
        ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
