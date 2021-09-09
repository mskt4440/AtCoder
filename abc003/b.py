#
# abc003 b
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
        input = """ch@ku@ai
choku@@i"""
        output = """You can win"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aoki
@ok@"""
        output = """You will lose"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """arc
abc"""
        output = """You will lose"""
        self.assertIO(input, output)


def resolve():
    S = input()
    T = input()

    l = len(S)
    w = ["a", "t", "c", "o", "d", "e", "r", "@"]
    ans = "You can win"
    for i in range(l):
        if S[i] == "@" and T[i] in w:
            continue
        if T[i] == "@" and S[i] in w:
            continue
        if S[i] != "@" and T[i] != "@" and S[i] == T[i]:
            continue
        ans = "You will lose"

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
