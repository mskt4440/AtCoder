#
# abc171 e
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
        input = """4
20 11 9 24"""
        output = """26 5 7 22"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    T = 0
    for a in A:
        T ^= a

    ans = []
    for a in A:
        ans.append(T ^ a)

    print(*ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
