#
# abc210 c
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
        input = """7 3
1 2 1 2 3 3 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
4 4 4 4 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 6
304621362 506696497 304621362 506696497 834022578 304621362 414720753 304621362 304621362 414720753"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    counter = collections.Counter(C[:K])
    ans = len(counter)
    for i in range(N-K):
        l = C[i]
        r = C[i+K]
        counter[l] -= 1
        counter[r] += 1
        if counter[l] == 0:
            del counter[l]
        ans = max(ans, len(counter))
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
