#
# abc181 c
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
0 1
0 2
0 3
1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14
5 5
0 1
2 5
8 0
2 1
0 0
3 6
8 6
5 9
7 9
3 4
9 2
9 8
7 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9
8 2
2 3
1 3
3 7
1 0
8 8
5 6
9 7
0 1"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    XY.sort(key=lambda x: (x[0], x[1]))
    ans = "No"
    for i in range(N):
        for j in range(i+1, N):
            dy = XY[j][1] - XY[i][1]
            for k in range(j+1, N):
                dx1 = XY[j][0] - XY[i][0]
                dy1 = XY[j][1] - XY[i][1]
                dx2 = XY[k][0] - XY[i][0]
                dy2 = XY[k][1] - XY[i][1]
                if dx1*dy2 == dx2*dy1:
                    ans = "Yes"
                    break
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
