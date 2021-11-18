#
# abc012 b
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
        input = """3661"""
        output = """01:01:01"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """86399"""
        output = """23:59:59"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    s = N % 60
    m = N % 3600 // 60
    h = N//3600
    print(str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2))


if __name__ == "__main__":
    # unittest.main()
    resolve()
