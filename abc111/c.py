#
# abc111 c
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
        input = """4
3 1 3 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
105 119 105 119 105 119"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 1 1 1"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    V = list(map(int, input().split()))

    O = []
    E = []
    for i, v in enumerate(V):
        if i % 2:
            O.append(v)
        else:
            E.append(v)

    OC = Counter(O).most_common(2)
    EC = Counter(E).most_common(2)

    ans = 0
    if OC[0][0] != EC[0][0]:
        ans = N - EC[0][1] - OC[0][1]
    else:
        if len(OC) == 1 or len(EC) == 1:
            ans = N//2
        else:
            ans = N - max(EC[0][1]+OC[1][1], EC[1][1]+OC[0][1])
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
