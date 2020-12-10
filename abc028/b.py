#
# abc028 b
#
import sys
from io import StringIO
import unittest
from collections import Counter


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
        input = """BEAF"""
        output = """1 1 0 0 1 1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """DECADE"""
        output = """1 0 1 2 2 0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """ABBCCCDDDDEEEEEFFFFFF"""
        output = """1 2 3 4 5 6"""
        self.assertIO(input, output)


def resolve():
    S = list(input())
    C = Counter(S)
    ans = [0]*6
    for k, v in C.items():
        if k == "A":
            ans[0] = v
        elif k == "B":
            ans[1] = v
        elif k == "C":
            ans[2] = v
        elif k == "D":
            ans[3] = v
        elif k == "E":
            ans[4] = v
        elif k == "F":
            ans[5] = v
    print(*ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
