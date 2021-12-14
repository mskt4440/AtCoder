#
# abc130 b
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
        input = """3 6
3 4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 9
3 3 3 3"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    p = 0
    ans = 1
    for l in L:
        p += l
        if p <= X:
            ans += 1
        else:
            break
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
