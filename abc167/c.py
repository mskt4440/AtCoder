#
# abc167 d
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
        input = """4 5
3 2 4 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 727202214173249351
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    F = [False]*N
    F[0] = True
    P = [0]
    p = 0
    for i in range(K):
        p = A[p]-1
        if F[p]:
            break
        P.append(p)
        F[p] = True

    d = P.index(p)
    ans = (K-d) % (len(P)-d)+d

    print(P[ans]+1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
