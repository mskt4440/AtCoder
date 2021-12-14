#
# abc108 c
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
        input = """3 2"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31415 9265"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """35897 932"""
        output = """114191"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())

    kn = 0
    k2 = 0
    for i in range(1, N+1):
        if i % K == 0:
            kn += 1
        if K % 2 == 0 and i % K == K//2:
            k2 += 1

    print(kn**3+k2**3)


if __name__ == "__main__":
    # unittest.main()
    resolve()
