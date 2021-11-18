#
# abc017 a
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

    def test_入力例1(self):
        input = """50 7
40 8
30 9"""
        output = """94"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """990 10
990 10
990 10"""
        output = """2970"""
        self.assertIO(input, output)


def resolve():
    SE = [list(map(int, input().split())) for _ in range(3)]
    ans = 0
    for s, e in SE:
        ans += s*e//10
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
