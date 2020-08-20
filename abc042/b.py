#
# abc042 b
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
        input = """3 3
dxx
axx
cxx"""
        output = """axxcxxdxx"""
        self.assertIO(input, output)


def resolve():
    N, L = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(input())
    S.sort()
    ans = ""
    for i in range(len(S)):
        ans += S.pop(0)
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
