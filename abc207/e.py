#
# abc207 e
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
        input = """4
1 2 3 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
8 6 3 3 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
791754273866483 706434917156797 714489398264550 918142301070506 559125109706263 694445720452148 648739025948445 869006293795825 718343486637033 934236559762733"""
        output = """15"""
        self.assertIO(input, output)


def resolve():


if __name__ == "__main__":
    unittest.main()
    # resolve()
