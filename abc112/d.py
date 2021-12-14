#
# abc112 d
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
        input = """3 14"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 123"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1000000000"""
        output = """10000"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())

    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= M:
        if M % i == 0:
            lower_divisors.append(i)
            if i != M // i:
                upper_divisors.append(M//i)
        i += 1
    L = lower_divisors + upper_divisors[::-1]
    L.sort(reverse=True)

    for l in L:
        if l > M//N:
            continue
        print(l)
        break


if __name__ == "__main__":
    # unittest.main()
    resolve()
