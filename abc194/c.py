#
# abc194 c
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

    def test_入力例_1(self):
        input = """3
2 8 4"""
        output = """56"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
-5 8 9 -4 -3"""
        output = """950"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    C = Counter(A)

    ans = 0
    for i in range(-200, 201):
        for j in range(i+1, 201):
            if i in C and j in C:
                ans += C[i]*C[j]*(i-j)**2
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
