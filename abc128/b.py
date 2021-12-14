#
# abc128 b
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
        input = """6
khabarovsk 20
moscow 10
kazan 50
kazan 35
moscow 60
khabarovsk 40"""
        output = """3
4
6
1
5
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
yakutsk 10
yakutsk 20
yakutsk 30
yakutsk 40
yakutsk 50
yakutsk 60
yakutsk 70
yakutsk 80
yakutsk 90
yakutsk 100"""
        output = """10
9
8
7
6
5
4
3
2
1"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    ISP = []
    for i in range(N):
        s, p = input().split()
        p = int(p)
        isp = [i+1, s, p]
        ISP.append(isp)

    ISP.sort(key=lambda x: (x[1], -x[2]))
    for i, s, p in ISP:
        print(i)


if __name__ == "__main__":
    # unittest.main()
    resolve()
