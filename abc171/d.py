#
# abc171 d
#
import sys
from io import StringIO
import unittest
import collections


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
        input = """4
1 2 3 4
3
1 2
3 4
2 4"""
        output = """11
12
16"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1
3
1 2
2 1
3 5"""
        output = """8
4
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1 2
3
1 100
2 100
100 1000"""
        output = """102
200
2000"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    s = sum(A)
    D = collections.defaultdict(int)
    for a in A:
        D[a] += 1

    for b, c in BC:
        if b in D:
            s += (c-b)*D[b]
            D[c] += D[b]
            D[b] = 0
        print(s)


if __name__ == "__main__":
    # unittest.main()
    resolve()
