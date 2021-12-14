#
# abc159 b
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
        input = """akasaka"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """level"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """atcoder"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    S = input()

    ans = "Yes"
    N = len(S)
    for i in range((N-1)//2):
        if S[i] != S[(N-1)//2-1-i]:
            ans = "No"
            break

    if ans == "Yes":
        for i in range((N+3)//2-1, N):
            if S[i] != S[N-1-i]:
                ans = "No"
                break

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
