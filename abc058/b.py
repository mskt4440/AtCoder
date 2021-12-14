#
# abc058 b
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
        input = """xyz
abc"""
        output = """xaybzc"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoderbeginnercontest
atcoderregularcontest"""
        output = """aattccooddeerrbreeggiunlnaerrccoonntteesstt"""
        self.assertIO(input, output)


def resolve():
    O = input()
    E = input()

    lo = len(O)
    le = len(E)
    ans = ""
    for i in range(le):
        ans += O[i]+E[i]
    if lo > le:
        ans += O[-1]

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
