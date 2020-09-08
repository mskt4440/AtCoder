#
# joi2007ho c
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
        input = """10
9 4
4 3
1 1
4 2
2 4
5 8
4 0
5 3
0 5
5 2"""
        output = """10"""
        self.assertIO(input, output)


def resolve():
    n = int(input())
    p = [tuple(map(int, input().split())) for _ in range(n)]
    setp = set(p)

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            a = abs(p[i][1]-p[j][1])
            b = abs(p[i][0]-p[j][0])
            p1 = (p[i][0]+a, p[i][1]+b)
            p2 = (p[j][0]+a, p[j][1]+b)
            if p1 in setp and p2 in setp:
                ans = max(ans, a**2+b**2)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
