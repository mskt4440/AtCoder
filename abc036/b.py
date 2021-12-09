#
# abc036 b
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
        input = """4
ooxx
xoox
xxxx
xxxx"""
        output = """xxxo
xxoo
xxox
xxxx"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = [input() for _ in range(N)]

    for i in range(N):
        for j in reversed(range(N)):
            print(S[j][i], end="")
        else:
            print()


if __name__ == "__main__":
    # unittest.main()
    resolve()
