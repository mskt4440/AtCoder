#
# abc084 c
#
import sys
from io import StringIO
from types import ClassMethodDescriptorType
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
6 5 1
1 10 1"""
        output = """12
11
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
12 24 6
52 16 4
99 2 2"""
        output = """187
167
101
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
12 13 1
44 17 17
66 4096 64"""
        output = """4162
4162
4162
0"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    CSF = [list(map(int, input().split())) for _ in range(N-1)]

    for i in range(N-1):
        t = CSF[i][1]+CSF[i][0]
        for c, s, f in CSF[i+1:]:
            if t > s:
                s += (t-s+f-1)//f*f
            t = s + c
        print(t)
    print(0)


if __name__ == "__main__":
    # unittest.main()
    resolve()
