#
# abc032 b
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
        input = """abcabc
2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """aaaaa
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """hello
10"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    s = input()
    k = int(input())

    l = len(s)
    if k > l:
        print(0)
    elif k == l:
        print(1)
    else:
        t = []
        for i in range(l-k+1):
            t.append(s[i:i+k])
        print(len(set(t)))


if __name__ == "__main__":
    # unittest.main()
    resolve()
