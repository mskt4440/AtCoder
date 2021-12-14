#
# abc110 c
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
        input = """azzel
apple"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """chokudai
redcoder"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcdefghijklmnopqrstuvwxyz
ibyhqfrekavclxjstdwgpzmonu"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    S = input()
    T = input()

    DS = {}
    DT = {}
    ans = "Yes"
    for s, t in zip(S, T):
        if s not in DS:
            DS[s] = t
        elif DS[s] != t:
            ans = "No"
            break

        if t not in DT:
            DT[t] = s
        elif DT[t] != s:
            ans = "No"
            break

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
