#
# abc158 d
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
        input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """y
1
2 1 x"""
        output = """xy"""
        self.assertIO(input, output)


def resolve():
    S = input()
    N = int(input())
    Q = [list(input().split()) for _ in range(N)]

    ans = "X"
    flag = True
    front = ""
    rear = ""
    for q in Q:
        if len(q) == 1:
            flag = not flag
        elif q[1] == "1":
            if flag:
                front += q[2]
            else:
                rear += q[2]
        else:
            if flag:
                rear += q[2]
            else:
                front += q[2]
    if flag:
        print(front[::-1]+S+rear)
    else:
        print(rear[::-1]+S[::-1]+front)


if __name__ == "__main__":
    # unittest.main()
    resolve()
