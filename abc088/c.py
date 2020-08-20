#
# abc088 c
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
        input = """1 0 1
2 1 2
1 0 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 2
2 1 2
2 2 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 8 8
0 8 8
0 8 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 8 6
2 9 7
0 7 7"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    c = []
    for _ in range(3):
        c.append(list(map(int, input().split())))

    a1 = 0
    b1 = c[0][0] - a1
    b2 = c[0][1] - a1
    b3 = c[0][2] - a1
    a2 = c[1][0] - b1
    a3 = c[2][0] - b1

    if a2+b2 == c[1][1] and a2+b3 == c[1][2] and a3+b2 == c[2][1] and a3+b3 == c[2][2]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
