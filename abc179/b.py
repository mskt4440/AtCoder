#
# abc179 b
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
1 2
6 6
4 4
3 3
3 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 1
2 2
3 4
5 5
6 6"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 1
2 2
3 3
4 4
5 5
6 6"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]

    n = 0
    for d in D:
        d1, d2 = d
        if d1 == d2:
            n += 1
            if n == 3:
                print("Yes")
                break
        else:
            n = 0
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
