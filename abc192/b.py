#
# abc192 b
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
        input = """dIfFiCuLt"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """eASY"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """a"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    S = input()

    ans = "Yes"
    for i in range(len(S)):
        if i % 2 and S[i].islower():
            ans = "No"
            break
        if i % 2 == 0 and S[i].isupper():
            ans = "No"
            break
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
