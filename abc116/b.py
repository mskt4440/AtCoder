#
# abc116 b
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
        input = """8"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """54"""
        output = """114"""
        self.assertIO(input, output)


def resolve():
    s = int(input())

    l = [s]
    i = 1
    while True:
        i += 1
        if l[-1] % 2:
            l.append(3*l[-1]+1)
        else:
            l.append(l[-1]//2)
        if l.count(l[-1]) >= 2:
            print(i)
            break


if __name__ == "__main__":
    # unittest.main()
    resolve()
