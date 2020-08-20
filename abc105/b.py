#
# abc105 b
#
import unittest
from io import StringIO
import sys


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
        input = """11"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """40"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    ans = "No"
    for i in range(N//4+1):
        for j in range(N//7+1):
            if 4*i + 7*j == N:
                ans = "Yes"
                break
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
