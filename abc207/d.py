#
# abc207 d
#
import sys
from io import StringIO
import unittest
import math


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
0 0
0 1
1 0
2 0
3 0
3 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 0
1 1
3 0
-1 0
-1 1
-3 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
0 0
2 9
10 -2
-6 -7
0 0
2 9
10 -2
-6 -7"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
10 5
-9 3
1 -5
-6 -5
6 9
-9 0
-7 -10
-10 -5
5 4
9 0
0 -10
-10 -2"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    CD = [(tuple(map(int, input().split())) for _ in range(N))]

    if (0, 0) not in set(AB):
        SAB = [(0, 0)]
        ox = AB[0]
        oy = AB[1]
        for x, y in AB[1:]:
            SAB.append((x-ox, y-oy))
        AB = SAB

    for p in range(1, 301):
        TAB = []
        for x, y in AB:
            r = math.radians(-p)
            nx = x*math.cos(r)-y*math.sin(r)
            ny = x*math.sin(r)+y*math.cos(r)
            TAB.append((int(nx), int(ny)))

            for dx, dy in CD:
                for x, y in TAB:
                    if x == 0 and y == 0:
                        continue
                    if x-dx == 0 and y-dy == 0:
                        continue

    print("No")


if __name__ == "__main__":
    unittest.main()
    # resolve()
