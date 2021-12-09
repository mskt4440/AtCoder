#
# abc035 b
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
        input = """UL?
1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """UD?
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """UUUU?DDR?LLLL
1"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """UULL?
2"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
    S = input()
    T = int(input())

    x = y = 0
    q = S.count("?")
    for i in range(len(S)):
        if S[i] == "?":
            continue
        if S[i] == "L":
            x -= 1
        elif S[i] == "R":
            x += 1
        elif S[i] == "U":
            y += 1
        elif S[i] == "D":
            y -= 1

    ans = abs(x)+abs(y)
    if T == 1:
        ans += q
    else:
        if ans > q:
            ans -= q
        elif (ans-q) % 2:
            ans = 1
        else:
            ans = 0

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
