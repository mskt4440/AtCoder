#
# abc044 b
#
import sys
from io import StringIO
import unittest
from collections import Counter


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
        input = """abaccaba"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """hthth"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    w = list(input())
    C = Counter(w)

    ans = "Yes"
    for k, v in C.items():
        if v % 2:
            ans = "No"
            break

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
