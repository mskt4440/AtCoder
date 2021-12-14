#
# abc177 d
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
        input = """5 3
1 2
3 4
5 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 10
1 2
2 1
1 2
2 1
1 2
1 3
1 4
2 3
2 4
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
3 1
4 1
5 9
2 6"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    R = []
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = min(a, b), max(a, b)
        if [a, b] not in R:
            R.append([a, b])

    E = [0] * N
    for r in R:
        E[r[0]-1] += 1
        E[r[1]-1] += 1

    print(max(E)+1)


if __name__ == "__main__":
    unittest.main()
