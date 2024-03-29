#
# abc093 b
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
        input = """3 8 2"""
        output = """3
4
7
8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 8 3"""
        output = """4
5
6
7
8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 9 100"""
        output = """2
3
4
5
6
7
8
9"""
        self.assertIO(input, output)


def resolve():
    A, B, K = map(int, input().split())

    ans = []
    for i in range(K):
        if A+i <= B and A+i not in ans:
            ans.append(A+i)
        if B-i >= A and B-i not in ans:
            ans.append(B-i)

    ans.sort()

    for a in ans:
        print(a)


if __name__ == "__main__":
    # unittest.main()
    resolve()
