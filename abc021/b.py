#
# abc021 b
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
1 5
3
3 4 2"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """7
1 3
4
2 4 2 7"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4
1 4
3
2 1 3"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4
1 4
3
2 4 3"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """20
1 4
12
2 3 5 7 8 9 10 11 12 15 13 14"""
        output = """YES"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    a, b = map(int, input().split())
    K = int(input())
    P = list(map(int, input().split()))

    ans = "YES"
    if len(P) != len(set(P)):
        ans = "NO"
    else:
        for p in P:
            if p == a or p == b:
                ans = "NO"
                break

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
