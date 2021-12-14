#
# abc066 b
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
        input = """abaababaab"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """xxxx"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcabcabcabc"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """akasakaakasakasakaakas"""
        output = """14"""
        self.assertIO(input, output)


def resolve():
    S = input()

    ans = 0
    for i in range(1, len(S)//2):
        if S[:i] == S[i:2*i]:
            ans = 2*i

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
