#
# abc111 b
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
        input = """111"""
        output = """111"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """112"""
        output = """222"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """750"""
        output = """777"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    for x in range(N, 1000):
        if str(x).count(str(x)[1]) == 3:
            print(x)
            break


if __name__ == "__main__":
    # unittest.main()
    resolve()
