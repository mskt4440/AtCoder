#
# s8pc6 b
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
        input = """3
5 7
2 6
8 10"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 71
43 64
13 35
14 54
79 85"""
        output = """334"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11
15004200 341668840
277786703 825590503
85505967 410375631
797368845 930277710
90107929 763195990
104844373 888031128
338351523 715240891
458782074 493862093
189601059 534714600
299073643 971113974
98291394 443377420"""
        output = """8494550716"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    AB = []
    A = []
    B = []
    D = 0
    for i in range(N):
        a, b = map(int, input().split())
        AB.append([a, b])
        A.append(a)
        B.append(b)
        D += b-a
    A.sort()
    B.sort()

    ans = float("inf")
    for s in A:
        for g in B:
            tmp = 0
            for ab in AB:
                a, b = ab
                tmp += abs(s-a)+abs(g-b)
            ans = min(ans, tmp)

    print(D+ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
