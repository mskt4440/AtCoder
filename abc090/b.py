#
# abc090 b
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
        input = """11009 11332"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """31415 92653"""
        output = """612"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())
    ans = 0
    for i in range(A, B+1):
        s = str(i)
        if s[0] == s[-1] and s[1] == s[-2]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
