#
# panasonic2020b d
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
        input = """1"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """aa
ab"""
        self.assertIO(input, output)


def resolve():
    global N
    N = int(input())

    dfs("a", "a")


def dfs(mw, s):
    if len(s) == N:
        print(s)
        return

    for i in range(ord(mw)-ord("a")+2):
        mw = max(mw, chr(ord("a")+i))
        ns = s + chr(ord("a")+i)
        dfs(mw, ns)


if __name__ == "__main__":
    # unittest.main()
    resolve()
