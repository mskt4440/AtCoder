#
# abc132 a
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
        input = """ASSA"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """STOP"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """FFEE"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """FREE"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    S = list(input())

    s = S[0]
    ans = "No"
    if S.count(s) == 2:
        S.remove(s)
        S.remove(s)
        if S[0] == S[1]:
            ans = "Yes"

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
