#
# abc087 b
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
        input = """2
2
2
100"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1
0
150"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
40
50
6000"""
        output = """213"""
        self.assertIO(input, output)


def resolve():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    ans = 0

    for i in range(A+1):
        if 500 * i > X:
            break
        for j in range(B+1):
            if X - 50 * C <= 500 * i + 100 * j <= X:
                ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
