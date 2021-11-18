#
# abc023 b
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
        input = """5
1
2
3
2
1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """11
3
1
4
1
5
9
2
6
5
3
5"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    C = Counter(A)
    ans = 0
    for v in C.values():
        if v >= 2:
            ans += v-1

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
