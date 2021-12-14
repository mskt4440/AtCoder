#
# abc097 c
#
import sys
from io import StringIO
import unittest
from collections import Counter


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
        input = """aba
4"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoderandatcodeer
5"""
        output = """andat"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """z
1"""
        output = """z"""
        self.assertIO(input, output)


def resolve():
    S = input()
    K = int(input())

    l = []
    for i in range(1, K+1):
        for j in range(len(S)-i+1):
            l.append(S[j:j+i])

    l = sorted(list(set(l)))
    print(l[K-1])


if __name__ == "__main__":
    # unittest.main()
    resolve()
