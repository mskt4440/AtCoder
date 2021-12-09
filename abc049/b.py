#
# abc049 b
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
        input = """2 2
*.
.*"""
        output = """*.
*.
.*
.*"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 4
***."""
        output = """***.
***."""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 20
.....***....***.....
....*...*..*...*....
...*.....**.....*...
...*.....*......*...
....*.....*....*....
.....**..*...**.....
.......*..*.*.......
........**.*........
.........**........."""
        output = """.....***....***.....
.....***....***.....
....*...*..*...*....
....*...*..*...*....
...*.....**.....*...
...*.....**.....*...
...*.....*......*...
...*.....*......*...
....*.....*....*....
....*.....*....*....
.....**..*...**.....
.....**..*...**.....
.......*..*.*.......
.......*..*.*.......
........**.*........
........**.*........
.........**.........
.........**........."""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    ans = []
    for i in range(H):
        S = input()
        ans.append(S)
        ans.append(S)

    for i in range(2*H):
        print(ans[i])


if __name__ == "__main__":
    # unittest.main()
    resolve()
