#
# abc157 b
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
        input = """84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """41 7 46
26 89 2
78 92 8
5
6
45
16
57
17"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    B = [int(input()) for _ in range(N)]

    T = [[0]*3 for _ in range(3)]

    for b in B:
        for i, a in enumerate(A):
            if b in a:
                T[i][a.index(b)] = 1

    ans = "No"
    for t in T:
        if not 0 in t:
            ans = "Yes"
            break
    else:
        for i in range(3):
            if T[0][i] == T[1][i] == T[2][i] == 1:
                ans = "Yes"
                break
        else:
            if T[0][0] == T[1][1] == T[2][2] == 1 or T[2][0] == T[1][1] == T[2][0] == 1:
                ans = "Yes"

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
