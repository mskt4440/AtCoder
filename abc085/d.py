#
# abc085 d
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
        input = """1 10
3 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 10
3 5
2 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 1000000000
1 1
1 10000000
1 30000000
1 99999999"""
        output = """860000004"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 500
35 44
28 83
46 62
31 79
40 43"""
        output = """9"""
        self.assertIO(input, output)


def resolve():
    N, H = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ma = max(A)
    B.sort(reverse=True)

    ans = 0
    for b in B:
        if H <= 0:
            break
        if b < ma:
            break
        H -= b
        ans += 1

    if H > 0:
        ans += (H+ma-1)//ma

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
