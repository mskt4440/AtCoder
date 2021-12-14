#
# abc141 b
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
        input = """RUDLUDR"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """DULL"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """UUUUUUUUUUUUUUU"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """ULURU"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """RDULULDURURLRDULRLR"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    S = input()

    ans = "Yes"
    for i in range(len(S)):
        if S[i] == "R" and i % 2:
            ans = "No"
            break
        if S[i] == "L" and i % 2 == 0:
            ans = "No"
            break
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
