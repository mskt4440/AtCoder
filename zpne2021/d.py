#
# zone2021 d
#
import sys
from io import StringIO
import unittest
from collections import deque


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
        input = """ozRnonnoe"""
        output = """zone"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """hellospaceRhellospace"""
        output = """"""
        self.assertIO(input, output)


def resolve():
    S = input()

    T = deque()
    f = True
    for w in S:
        if w == "R":
            if f:
                f = False
            else:
                f = True
        else:
            if f:
                if T and w == T[-1]:
                    T.pop()
                else:
                    T.append(w)
            else:
                if T and w == T[0]:
                    T.popleft()
                else:
                    T.appendleft(w)

    if not f:
        T = reversed(T)
    print("".join(T))


if __name__ == "__main__":
    # unittest.main()
    resolve()
