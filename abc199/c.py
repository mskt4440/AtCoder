#
# abc199 c
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
        input = """2
FLIP
2
2 0 0
1 1 4"""
        output = """LPFI"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4"""
        output = """ILPF"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = input()
    Q = int(input())
    TAB = [list(map(int, input().split())) for _ in range(Q)]

    LS = list(S)
    f = True
    for t, a, b in TAB:
        if t == 1:
            if f:
                LS[a-1], LS[b-1] = LS[b-1], LS[a-1]
            else:
                if a <= N:
                    a += N
                else:
                    a -= N
                if b <= N:
                    b += N
                else:
                    b -= N
                LS[a-1], LS[b-1] = LS[b-1], LS[a-1]
        else:
            if f:
                f = False
            else:
                f = True

    if f == False:
        LS = LS[N:]+LS[:N]

    for ls in LS:
        print(ls, end="")
    print()


if __name__ == "__main__":
    # unittest.main()
    resolve()
