#
# arc007 b
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
        input = """5 6
2
3
5
0
1
3"""
        output = """0
5
2
4
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
0
1
1
1
2"""
        output = """0
1
3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 0"""
        output = """1
2
3
4
5"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 7
2
8
5
3
3
8
1"""
        output = """8
0
5
4
3
6
7
2
9
10"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """5 7
3
4
3
1
2
2
0"""
        output = """3
1
2
4
5"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    D = [int(input()) for _ in range(M)]

    C = [i+1 for i in range(N)]
    n = 0
    for d in D:
        if d == n:
            continue
        C[C.index(d)] = n
        n = d

    for c in C:
        print(c)


if __name__ == "__main__":
    # unittest.main()
    resolve()
