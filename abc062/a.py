#
# abc062 a
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
        input = """1 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 4"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    x, y = map(int, input().split())

    g1 = set([1, 3, 5, 7, 8, 10, 12])
    g2 = set([4, 6, 9, 11])
    g3 = set([2])

    if x in g1 and y in g1:
        print("Yes")
    elif x in g2 and y in g2:
        print("Yes")
    elif x in g3 and y in g3:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # unittest.main()
    resolve()
