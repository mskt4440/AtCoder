#
# abc168 c
#
import sys
from io import StringIO
import unittest
import collections


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
        input = """4 4
1 2
2 3
3 4
4 2"""
        output = """Yes
1
2
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6"""
        output = """Yes
6
5
5
1
1"""
        self.assertIO(input, output)


def resolve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    G = [[]*N for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    q = collections.deque()
    ans = [-1]*N
    ans[0] = 0
    p = 0
    q.append(p)
    while q:
        p = q.popleft()
        for n in G[p]:
            if ans[n] != -1:
                continue
            ans[n] = p
            q.append(n)

    if -1 in ans:
        print("No")
    else:
        print("Yes")
        for a in ans[1:]:
            print(a+1)


if __name__ == "__main__":
    # unittest.main()
    resolve()
