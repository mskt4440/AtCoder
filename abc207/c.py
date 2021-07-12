#
# abc207 c
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
1 1 2
2 2 3
3 2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """19
4 210068409 221208102
4 16698200 910945203
4 76268400 259148323
4 370943597 566244098
1 428897569 509621647
4 250946752 823720939
1 642505376 868415584
2 619091266 868230936
2 306543999 654038915
4 486033777 715789416
1 527225177 583184546
2 885292456 900938599
3 264004185 486613484
2 345310564 818091848
1 152544274 521564293
4 13819154 555218434
3 507364086 545932412
4 797872271 935850549
2 415488246 685203817"""
        output = """102"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    TLR = [list(map(int, input().split())) for _ in range(N)]

    LR = []
    for t, l, r in TLR:
        if t == 1:
            LR.append([l*10, r*10])
        elif t == 2:
            LR.append([l*10, r*10-1])
        elif t == 3:
            LR.append([l*10+1, r*10])
        elif t == 4:
            LR.append([l*10+1, r*10-1])

    ans = 0
    for i, lr in enumerate(LR):
        l1 = lr[0]
        r1 = lr[1]
        for l2, r2 in LR[i+1:]:
            if r2 < l1 or r1 < l2:
                continue
            ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
