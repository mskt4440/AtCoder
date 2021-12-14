#
# abc198 d
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
        input = """a
b
c"""
        output = """1
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """x
x
y"""
        output = """1
1
2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """p
q
p"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """abcd
efgh
ijkl"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """send
more
money"""
        output = """9567
1085
10652"""
        self.assertIO(input, output)


def resolve():


if __name__ == "__main__":
    unittest.main()
    # resolve()
