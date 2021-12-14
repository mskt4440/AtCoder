#
# arc105 d
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
        input = """3
1
10
2
1 2
21
476523737 103976339 266993 706803678 802362985 892644371 953855359 196462821 817301757 409460796 773943961 488763959 405483423 616934516 710762957 239829390 55474813 818352359 312280585 185800870 255245162"""
        output = """Second
First
Second"""
        self.assertIO(input, output)


def resolve():
    TN = int(input())
    TC = []
    for i in range(TN):
        N = int(input())
        A = [N]
        A += list(map(int, input().split()))
        TC.append(A)

    for tc in TC:
        n, *T = tc


if __name__ == "__main__":
    unittest.main()
    # resolve()
