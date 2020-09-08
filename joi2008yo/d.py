#
# joi2008yo d
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
        input = """5
8 5
6 4
4 3
7 10
0 10
10
10 5
2 7
9 7
8 10
10 2
1 2
8 1
6 7
6 0
0 9"""
        output = """2 -3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
904207 809784
845370 244806
499091 59863
638406 182509
435076 362268
10
757559 866424
114810 239537
519926 989458
461089 424480
674361 448440
81851 150384
459107 795405
299682 6700
254125 362183
50795 541942"""
        output = """-384281 179674"""
        self.assertIO(input, output)


def resolve():
    m = int(input())
    T = [tuple(map(int, input().split())) for _ in range(m)]
    n = int(input())
    P = [tuple(map(int, input().split())) for _ in range(n)]
    setp = set(P)

    D = []
    ox, oy = T[0]
    for t in T[1:]:
        x, y = t
        D.append([x-ox, y-oy])

    for p in P:
        x, y = p
        dx = x - ox
        dy = y - oy
        for d in D:
            tx, ty = d
            tx += x
            ty += y
            if (tx, ty) not in setp:
                break
        else:
            print(f"{dx} {dy}")
            break


if __name__ == "__main__":
    # unittest.main()
    resolve()
