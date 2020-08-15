#
# abc083 b
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
        input = """20 2 5"""
        output = """84"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 1 2"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 4 16"""
        output = """4554"""
        self.assertIO(input, output)


def resolve():
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(N+1):
        t = str(i)
        s = 0
        for j in range(len(t)):
            s += int(t[j])
        if A <= s <= B:
            ans += i
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
