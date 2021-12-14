#
# abc191 b
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
        input = """5 5
3 5 6 5 4"""
        output = """3 6 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
3 3 3"""
        output = """"""
        self.assertIO(input, output)


def resolve():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = []
    for i in range(N):
        if A[i] != X:
            ans.append(A[i])
    print(*ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
