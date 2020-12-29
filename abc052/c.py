#
# abc052 c
#
import sys
from io import StringIO
import unittest
from unittest.case import doModuleCleanups


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
        input = """3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000"""
        output = """972926972"""
        self.assertIO(input, output)


def resolve():
    N = int(input())

    PL = []
    NPL = []
    for i in range(2, N+1):
        if i not in NPL:
            PL.append(i)
        for j in range(2, N+1):
            NPL.append(i*j)
            if i*j > N:
                break

    PN = [0]*len(PL)
    for i in range(1, N+1):
        t = i
        for j, pl in enumerate(PL):
            while t > 1:
                if t % pl:
                    break
                else:
                    PN[j] += 1
                    t //= pl

    ans = 1
    for pn in PN:
        if pn == 0:
            continue
        ans *= pn+1
    print(ans % (10**9+7))


if __name__ == "__main__":
    # unittest.main()
    resolve()
