#
# abc076 b
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
3"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
10"""
        output = """76"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    K = int(input())

    ans = 1
    for i in range(N):
        ans = min(2*ans, ans+K)

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
