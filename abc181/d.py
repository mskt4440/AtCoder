#
# abc181 d
#
import sys
from io import StringIO
import unittest
from collections import Counter


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
        input = """1234"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1333"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():

    n = input()

    if len(n) <= 2:
        if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        exit()

    cnt = Counter(n)

    for i in range(112, 1000, 8):
        tmp = Counter(str(i)) - cnt
        print(tmp)
        if not tmp:
            print("Yes")
            break


if __name__ == "__main__":
    unittest.main()
    # resolve()
