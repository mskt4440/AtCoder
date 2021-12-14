#
# abc113 c
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
        input = """2 3
1 32
2 63
1 12"""
        output = """000001000002
000002000001
000001000001"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
2 55
2 77
2 99"""
        output = """000002000001
000002000002
000002000003"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    IPY = []
    for i in range(M):
        IPY.append([i] + list(map(int, input().split())))

    F = [0]*N
    ANS = [""]*M
    IPY.sort(key=lambda x: x[2])
    for ipy in IPY:
        i, p, y = ipy
        F[p-1] += 1
        ANS[i] = str(p).zfill(6)+str(str(F[p-1]).zfill(6))

    for ans in ANS:
        print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
