#
# arc014 b
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
ab
ba
ab
cb"""
        output = """LOSE"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
atcoder
redcoder
recorder"""
        output = """DRAW"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    W = [input() for _ in range(N)]

    F = [W[0]]
    for i in range(1, N):
        if W[i] in F or W[i][0] != W[i-1][-1]:
            if i % 2:
                print("WIN")
                break
            else:
                print("LOSE")
                break
        F.append(W[i])
    else:
        print("DRAW")


if __name__ == "__main__":
    # unittest.main()
    resolve()
