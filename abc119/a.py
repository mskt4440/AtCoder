#
# abc119 a
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
        input = """2019/04/30"""
        output = """Heisei"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2019/11/01"""
        output = """TBD"""
        self.assertIO(input, output)


def resolve():
    S = list(map(int, input().split("/")))

    if S[0] < 2018:
        print("Heisei")
    elif S[0] > 2020:
        print("TBD")
    else:
        if S[1] <= 4:
            print("Heisei")
        else:
            print("TBD")


if __name__ == "__main__":
    # unittest.main()
    resolve()
