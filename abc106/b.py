#
# abc106 b
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
        input = """105"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    ans = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            continue
        t = 0
        for j in range(1, N+1):
            if i % j == 0:
                t += 1
        if t == 8:
            ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
