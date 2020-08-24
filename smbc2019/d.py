#
# smbc2019 d
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
        input = """4
0224"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
123123"""
        output = """17"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """19
3141592653589793238"""
        output = """329"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = input()

    ans = 0
    o = []
    for i in range(10):
        ip = S.find(str(i))
        if ip >= N-2 or ip == -1:
            continue
        for j in range(10):
            jp = S[ip+1:].find(str(j))
            if jp == -1:
                continue
            if ip + 1 + jp >= N-1:
                continue
            jp += ip+1
            for k in range(10):
                kp = S[jp+1:].find(str(k))
                if kp == -1:
                    continue
                t = str(i)+str(j)+str(k)
                if t not in o:
                    ans += 1
                    o.append(t)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
