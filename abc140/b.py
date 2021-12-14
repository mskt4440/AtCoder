#
# abc140 b
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
        input = """3
3 1 2
2 5 4
3 6"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
2 3 4 1
13 5 8 24
45 9 15"""
        output = """74"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1 2
50 50
50"""
        output = """150"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    l = -10
    ans = 0
    for a in A:
        ans += B[a-1]
        if l+1 == a:
            ans += C[l-1]
        l = a
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
