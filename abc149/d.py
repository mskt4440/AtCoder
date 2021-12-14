#
# abc149 d
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
        input = """5 2
8 7 6
rsrpr"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 1
100 10 1
ssssppr"""
        output = """211"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr"""
        output = """4996"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    score = {"r": P, "s": R, "p": S}
    target = [[] for _ in range(K)]
    for i, t in enumerate(T):
        target[i % K].append(t)

    ans = 0
    for t in target:
        ans += score[t[0]]
        l = t[0]
        for i in range(1, len(t)):
            if t[i] == l:
                l = None
                continue
            else:
                ans += score[t[i]]
                l = t[i]
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
