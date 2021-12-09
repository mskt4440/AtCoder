#
# abc036 c
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

    def test_入力例1(self):
        input = """5
3
3
1
6
1"""
        output = """1
1
0
2
0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    T = sorted(list(set(A)))

    D = {}
    for i, t in enumerate(T):
        D[t] = i

    for a in A:
        print(D[a])


if __name__ == "__main__":
    # unittest.main()
    resolve()
