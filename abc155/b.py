#
# abc155 b
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
6 7 9 10 31"""
        output = """APPROVED"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
28 27 24"""
        output = """DENIED"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = "APPROVED"
    for a in A:
        if a % 2:
            continue
        if a % 3 and a % 5:
            ans = "DENIED"
            break
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
