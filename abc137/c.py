#
# abc137 c
#
import sys
from io import StringIO
import unittest
from collections import Counter
import math


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
        input = """3
acornistnt
peanutbomb
constraint"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
oneplustwo
ninemodsix"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = []
    for i in range(N):
        s = list(input())
        s.sort()
        S.append("".join(s))

    C = Counter(S)
    ans = 0
    for i in C.values():
        if i == 1:
            continue
        ans += math.factorial(i)//(math.factorial(i-2)*math.factorial(2))
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
