#
# abc148 b
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
        input = """2
ip cc"""
        output = """icpc"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
hmhmnknk uuuuuuuu"""
        output = """humuhumunukunuku"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
aaaaa aaaaa"""
        output = """aaaaaaaaaa"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S, T = map(str, input().split())

    ans = ""
    for s, t in zip(S, T):
        ans += s+t
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
