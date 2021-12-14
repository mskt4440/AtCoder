#
# abc158 c
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
        input = """2 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 10"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """19 99"""
        output = """-1"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    for i in range(1, 1010):
        if int(i*0.08) == A and int(i*0.1) == B:
            print(i)
            break
    else:
        print(-1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
