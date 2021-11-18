#
# abc019 b
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
        input = """aabbbaad"""
        output = """a2b3a2d1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """aabbbbbbbbbbbbxyza"""
        output = """a2b12x1y1z1a1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """edcba"""
        output = """e1d1c1b1a1"""
        self.assertIO(input, output)


def resolve():
    s = list(input())

    ans = s[0]
    n = 1
    for w in s[1:]:
        if w == ans[-1]:
            n += 1
        else:
            ans += str(n) + w
            n = 1
    else:
        ans += str(n)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
