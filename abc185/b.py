#
# abc185 b
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
        input = """10 2 20
9 11
13 17"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2 20
9 11
13 16"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 3 30
5 8
15 17
24 27"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20 1 30
20 29"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """20 1 30
1 10"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    ans = "Yes"
    c = N
    t = 0
    for a, b, in AB:
        c = c-a+t
        t = a
        if c <= 0:
            ans = "No"
            break
        c = min(c+b-t, N)
        t = b
    c = c-T+t
    if c <= 0:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
