#
# abc155 c
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
        input = """7
beat
vet
beet
bed
vet
bet
beet"""
        output = """beet
vet"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo"""
        output = """buffalo"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
bass
bass
kick
kick
bass
kick
kick"""
        output = """kick"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
ushi
tapu
nichia
kun"""
        output = """kun
nichia
tapu
ushi"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = [input() for _ in range(N)]

    C = Counter(S)
    t = C.most_common()[0][1]
    ans = []
    for k, v in C.most_common():
        if v == t:
            ans.append(k)
    ans.sort()
    for a in ans:
        print(a)


if __name__ == "__main__":
    # unittest.main()
    resolve()
