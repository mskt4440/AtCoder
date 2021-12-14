#
# abc135 b
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
        input = """5
5 2 3 4 1"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2 4 3 5 1"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1 2 3 4 5 6 7"""
        output = """YES"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    P = list(map(int, input().split()))

    D = []
    for i, p in enumerate(P, 1):
        if p == i:
            continue
        D.append(p)
    if len(D) == 0 or len(D) == 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # unittest.main()
    resolve()
