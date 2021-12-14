#
# abc209 e
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
        input = """3
abcd
bcda
ada"""
        output = """Aoki
Takahashi
Draw"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
ABC"""
        output = """Draw"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
eaaaabaa
eaaaacaa
daaaaaaa
eaaaadaa
daaaafaa"""
        output = """Takahashi
Takahashi
Takahashi
Aoki
Takahashi"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = [input() for _ in range(N)]


if __name__ == "__main__":
    unittest.main()
    # resolve()
