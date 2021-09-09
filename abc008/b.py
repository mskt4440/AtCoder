#
# abc008 b
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

    def test_入力例1(self):
        input = """4
taro
jiro
taro
saburo"""
        output = """taro"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1
takahashikun"""
        output = """takahashikun"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """9
a
b
c
c
b
c
b
d
e"""
        output = """b"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = [input() for _ in range(N)]
    c = Counter(S)
    print(c.most_common()[0][0])


if __name__ == "__main__":
    # unittest.main()
    resolve()
