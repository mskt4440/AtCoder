#
# abc191 c
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
.....
.###.
.###.
.###.
....."""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    L = [0]*H
    for i in range(H):
        for j in range(W):
            if A[i, j] == ".":
                continue
            L += 1


if __name__ == "__main__":
    unittest.main()
    # resolve()
