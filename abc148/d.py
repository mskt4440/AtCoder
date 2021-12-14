#
# abc148 d
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
2 1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2 2 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
3 1 4 1 5 9 2 6 5 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    t = 1
    R = []
    ans = 0
    for a in A:
        if a != t:
            ans += 1
        else:
            R.append(t)
            t += 1
    if not R:
        ans = -1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
