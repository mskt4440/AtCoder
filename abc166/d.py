#
# abc166 d
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
        input = """33"""
        output = """2 -1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0 -1"""
        self.assertIO(input, output)


def resolve():
    X = int(input())

    flag = False
    for a in range(-118, 120):
        for b in range(-118, 120):
            if a**5 - b**5 == X:
                print(a, b)
                flag = True
                break
        if flag == True:
            break


if __name__ == "__main__":
    # unittest.main()
    resolve()
