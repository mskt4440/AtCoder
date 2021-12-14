#
# abc199 d
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
        input = """3 3
1 2
2 3
3 1"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 0"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 6
1 2
2 3
3 4
2 4
1 3
1 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20 0"""
        output = """3486784401"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(m)]

    G = [[]*N for _ in range(N)]
    for a, b in ab:
        G.append(a-1) = b-1
        G.append(b-1) = a-1


if __name__ == "__main__":
    unittest.main()
    # resolve()
