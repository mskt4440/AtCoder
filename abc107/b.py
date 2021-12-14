#
# abc107 b
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
        input = """4 4
##.#
....
##.#
.#.#"""
        output = """###
###
.##"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
#..
.#.
..#"""
        output = """#..
.#.
..#"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
.....
.....
..#..
....."""
        output = """#"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 6
......
....#.
.#....
..#...
..#...
......
.#..#."""
        output = """..#
#..
.#.
.#.
#.#"""
        self.assertIO(input, output)


def resolve():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    A = list(zip(*A))
    x = 0
    for a in A:
        if "#" in a:
            continue
        else:
            x += 1
    if x:
        for _ in range(x):
            A.remove(tuple("."*H))

    y = 0
    A = list(zip(*A))
    for a in A:
        if "#" in a:
            continue
        else:
            y += 1
    if y:
        for _ in range(y):
            A.remove(tuple("."*(W-x)))

    for a in A:
        print(*a, sep="")


if __name__ == "__main__":
    # unittest.main()
    resolve()
