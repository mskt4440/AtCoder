#
# abc076 c
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
        input = """?tc????
coder"""
        output = """atcoder"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """??p??d??
abc"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)


def resolve():
    S = input()
    T = input()

    ls = len(S)
    lt = len(T)

    ans = "UNRESTORABLE"
    for i in range(ls-lt+1):
        for j in range(lt):
            if S[i+j] == "?" or S[i+j] == T[j]:
                continue
            break
        else:
            ans = S[:i] + T + S[i+lt:]
    else:
        ans = ans.replace("?", "a")

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
