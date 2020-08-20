#
# abc065 b
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
3
1
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    a = [0] + [int(input()) for _ in range(N)]
    A = [0] * (N+1)

    p = 1
    ans = 0
    while True:
        A[p] += 1
        if A[p] == 2:
            ans = "-1"
            break
        ans += 1
        p = a[p]
        if p == 2:
            break

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
