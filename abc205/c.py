#
# abc205 c
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
        input = """3 2 4"""
        output = """>"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-7 7 2"""
        output = """="""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """-8 6 3"""
        output = """<"""
        self.assertIO(input, output)


def resolve():
    A, B, C = map(int, input().split())

    if C % 2:
        if A == B:
            print("=")
        elif (A > 0 and B > 0) or (A < 0 and B < 0):
            print(">")
        else:
            if A > B:
                print(">")
            else:
                print("<")
    else:
        if abs(A) == abs(B):
            print("=")
        elif abs(A) > abs(B):
            print(">")
        else:
            print("<")


if __name__ == "__main__":
    # unittest.main()
    resolve()
