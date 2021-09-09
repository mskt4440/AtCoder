#
# abc005 c
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
        input = """1
3
1 2 3
3
2 3 4"""
        output = """yes"""

        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
3
1 2 3
3
2 3 5"""
        output = """no"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
3
1 2 3
10
1 2 3 4 5 6 7 8 9 10"""
        output = """no"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
3
1 2 3
3
1 2 2"""
        output = """no"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """2
5
1 3 6 10 15
3
4 8 16"""
        output = """yes"""
        self.assertIO(input, output)


def resolve():
    T = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    ans = "yes"
    if M > N:
        ans = "no"
    else:
        x = 0
        for b in B:
            for i, a in enumerate(A[x:]):
                if a <= b <= a+T:
                    x += i+1
                    break
            else:
                ans = "no"
                break

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
